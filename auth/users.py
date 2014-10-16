#!/usr/bin/python3
# 项目：用户管理模块
# 名称：QT5库函数
# 作者：黄涛
# 创建：2014-8-6
from work.basefrm import TransFrame
from mylib.djpwd import make_password,check_password
class Login(TransFrame):
    sql='select password from auth_user where username=%s'
    def init(self):
        self['useritems']=self.enum_user()
        self.initial.update(self.user_cnf())
        self.initial['autologin']=int(self.initial['autologin'])
        super().init()
    
    def check(self):
        pwd=self.query_str(self.sql,params=self['teller,'])
        if pwd is None:
            raise Exception('用户不存在！')
        if not check_password(self['passwd'],pwd):
            raise Exception('密码不正确！')
    
    def post(self):
        def get_perms(cur):
            self['permissions']=[r[0] for r in cur]
        self.call_proc('get_permissions',args=self['teller,result'],proc=get_perms)
        extra=self.datas('teller,permissions')
        self.notify('',extra)
        self.user_cnf(self['user'],self.datas('user,passwd,autologin'))
        self.close()
                
class ChangePwd(TransFrame):
    sql='update auth_user set password=%s where username=%s'
    
    def check(self):
        if self['newpwd']!=self['cfmpwd']:
            raise Exception('两次输入密码不一致')
        pwd=self.query_str(Login.sql,params=(self.teller,))
        if pwd is None:
            raise Exception('用户不存在！')
        if not check_password(self['passwd'],pwd):
            raise Exception('原密码不正确！')
        if len(self['newpwd'])<6:
            raise Exception('新密码长度不得小于6位')
    
    def post(self):
        newpwd=make_password(self['newpwd'])
        self.execute(self.sql,(newpwd,self.teller))           
        self.showinfo('修改密码成功！')
        self.close()
   


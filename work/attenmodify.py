# 项目：营运管理平台
# 模块：考勤数据调整
# 作者：黄涛
# 创建：2013-8-7
# 修改：2013-8-8 增加了values方法
# 修改：2013-9-4 修改了查询方法，解决了没有对应日期，系统无法处理的BUG
from .basefrm import TransFrame
from datetime import datetime
class AttenModify(TransFrame):

    def init(self):
        n=datetime.today()
        y,m=n.year,n.month-1
        if m==0:
            y,m=y-1,12
        self['date']='%04d-%02d-01'%(y,m)

    def submit(self):
        if self['enter_time'] and self['exit_time']:
            asql='replace into attendance(Entertime,ExitTime,id,name,date)'\
                    'values(%s,%s,%s,%s,%s)'
            self.execute(asql,params=self['enter_time,exit_time,id,'\
                    'name,date']) 
            self.showinfo('修改成功！')
    
    def query(self,event):
        asql='select Entertime,ExitTime from attendance '\
            'where id=%s and date=%s' 
        user_id=self.query_str('select id from renyuanxinxi where '\
                'xingming=%s',params=self['name,'])
        if user_id:
            self['id']=user_id
            self['enter_time,exit_time']=\
                    self.query_list(asql,params=self['id,date'],direction=1)

        

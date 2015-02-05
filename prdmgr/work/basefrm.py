# Copyright(C) 2013 Huangtao
#
# 营运管理程序
# 模块：基础类
# 作者：黄涛
# 创建：2013-5-26
# 修订：2014-07-22 对调用Mysql的方式进行调整
# 修订：2014-8-8 对submit 函数进行修订
from qtgui import Window 
#from mylib.my import Mysql
from stdlib import MyMgr,Config
#from mylib.xmlfile import Config
from datetime import date

class TransFrame(Window,MyMgr,Config):
    
    @property
    def teller(self):
        return self['teller']
    @teller.setter
    def teller(self,teller):
        self['teller']=teller
    
    def post(self):
        pass
        
    def check(self):
        pass
        
    def submit(self):
        try:
            self.check()
            self.post()
        except Exception as e:
            self.showerr(str(e))

    def reg_journal(self,tr_code,memo):
        self.call_proc('Regjournal',params=(self.teller,tr_code,memo))
    
    def __general_list(self,begin,step,base,width,count):
        return tuple("%s-%s"%(begin//base,str(begin%base+1).zfill(width))\
                for begin in range(begin,begin+step*count,step))

    def create_month_list(self,begin_date=None,count=12,step=-1):
        '''生成月份列表'''
        begin_date=begin_date or date.today()
        m=begin_date.year*12+begin_date.month-1+step
        return self.__general_list(m,step,12,2,count)

    def create_quarter_list(self,begin_date=None,count=4,step=-1):
        '''生成季度列表'''
        begin_date=begin_date or date.today()
        q=begin_date.year*4+int(begin_date.month/3)+step
        return self.__general_list(q,step,4,1,count)

    def get_spell(self,string):
        '''获取字符串中汉字拼音的首字母'''
        return self.query_str('select getpy(%s)',params=(string,))
    
    def query_data(self,sql,params=None,multi=None):
        r=self.query(sql,params)
        return r.fetchall()

class TrFrame(TransFrame):

    @property
    def proc_name(self):
        return(self['__proc_name'])

    @proc_name.setter
    def proc_name(self,value):
        self['__proc_name']=value

    @property
    def result(self):
        return(self['__result'])

    @result.setter
    def result(self,value):
        self['__result']=value

    @property
    def param_list(self):
        return self['__param_list']

    @param_list.setter
    def param_list(self,value):
        self['__param_list']=value

    def post(self):
        if self.proc_name:
            self[self.param_list]=self.call_proc(\
                    self.proc_name,self[self.param_list],\
                    call_back=self.proc_result)
            if self.result:
                self.failed()
            else:
                self.success()
   
    def success(self):
        self.showinfo('提交成功')
    
    def failed(self):
        self.showerr('提交失败') 

    def proc_result(self,cursor):
        pass

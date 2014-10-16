from .basefrm import TrFrame 
class Login(TrFrame):

    def init(self):
        self['autologin']=2
        self.proc_name='Login'
        self.param_list='user,passwd,username,dept,group,__result'
    def success(self):
        self.notify(login=self['user,username,dept,group'])
        self.close()

#!/usr/bin/python3
# 项目：营运管理平台
# 模块：主模块
# 作者：黄涛
# 创建：2014-08-04 新的命令管理器，使用qtgui模块
#from mylib.qtgui import QtGui,MainWindow
from qtgui import MdiWindow
from os.path import expanduser,dirname,join
#from mylib.my import Mysql
from mymgr import MyMgr
from mylib.xmlfile import Config
import sys

class Window(MdiWindow,MyMgr,Config):  #主窗口
    base_dir=dirname(__file__)   #文件路径
    sys.path.append(base_dir)
    from settings import apps,comm_app
    comm_app=comm_app
    apps=apps                    #子窗口
    title='营运管理平台 Ver 1.0'  #窗口标题
    ui_file=join(base_dir,'workmgr.gui')  #UI资源文件名
    def init(self):
        self.widget.resize(960,600)
        self.open_config(join(self.base_dir,'prdmgr.xml'))  #打开配置文件
        self.connect(**self.my_cnf())  #连接数据库
        self.teller=''
        super().init()    
        login=self.add_child('auth.users.Login')
        if login['autologin']=='2':
            login.submit()
        else:
            self.notify('',{})

    def proc_permissions(self,permissions):
        if not permissions:
            permissions=[]

        for app,action in self.app_list.items():
            action.setVisible(app in permissions)                
                
    def notify(self,msg,extra=None):  #通知函数
        self['db'] ='已连接' if self.connected else '未连接'
        if extra is not None:
            self.teller=extra.get('teller','')
            self.proc_permissions(extra.get('permissions',self.comm_app))
            self.Logout.setVisible(self.teller!='')
        self['user']=self.teller            
        self.status_bar.showMessage(msg)
                
    def create_widget(self,name):    #创建子窗口
        widget=super().create_widget(name)
        if widget:
            widget['teller']=self.teller
            widget.notify=self.notify
            widget.add_child=self.add_child
            widget.base_dir=self.base_dir
            return widget
    
    def logout(self):
        self.notify('签退成功',{})
    
if __name__=='__main__':
    #QtGui.main(Window)
    Window.run()

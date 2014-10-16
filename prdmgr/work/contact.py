# Copyright(c) 2014 Huangtao
# 项目：营运管理平台
# 模块：通讯录
# 作者：黄涛
# 创建：2014-04-05
from .basefrm import TrFrame
class Contact(TrFrame):
    def init(self):
        pass
    def item_changed(self,row,col):
        print((row,col,))

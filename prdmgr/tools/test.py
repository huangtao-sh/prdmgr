# Copyrght(C) 2014 Huangtao
# 项目：营运管理平台
# 模块：测试模块
# 作者：黄涛
# 创建：2014-08-04
from work.basefrm import TransFrame
from PyQt5.QtWidgets import *
class Test(TransFrame):
    initial={'provs':[(1,'收到'),(2,'付出'),(3,'来到'),(4,'清空'),(5,'清空'),
        (7,'收到'),(8,'付出'),(9,'来到'),(10,'清空')],
        }
    
    def init(self):
        super().init()
        self['val']=[3,4,5,7]
        
    def check(self):
        if 1 :
            raise Exception('Hello world')
    
    def post(self):
        pass

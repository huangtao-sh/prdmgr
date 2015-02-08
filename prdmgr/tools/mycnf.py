# Copyrght(C) 2015 Huangtao
# 项目：营运管理平台
# 模块：数据库配置
# 作者：黄涛
# 创建：2015-2-8
from work.basefrm import TrFrame
class MySQLConfig(TrFrame):
    def init(self):
        self['cfglist']=self.enum_mysql()

    def submit(self):
        pass

    def cfg_change(self):
        showinf(self['cur'])

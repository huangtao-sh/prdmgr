# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：营运主管考核数据导出模块
# 作者：黄涛
# 创建：2013-12-4
# 修改：2013-12-6 新增会计主管季度考核报表导出功能
# 修改：2013-12-7 使用xlsxwriter来填写EXCEL
# 修改：2013-12-16使用Table来填写Excel
# 修改：2014-02-24 使用QT作为主控程序
from work.basefrm import TrFrame
from xlsxwriter import *
class Kaohe(TrFrame):
    def init(self):
        self['months']=self.create_quarter_list()
        self.proc_name='kaohe'
        self.param_list='zhangqi,result'

    def proc_result(self,cursor):
        wb=Workbook('营运主管考核%s.xlsx'\
                %(self['zhangqi']))
        ws=wb.add_worksheet('营运主管考核')
        hs_style=wb.add_format({'num_format':'0.0',
            'border':1})
        border=wb.add_format({'border':1})
        columns=[{'header':'分行名称','format':border},
                {'header':'银企对账回收率',
                    'format':hs_style},
                {'header':'电子对账签约率','format':hs_style}]
        ws.set_column('A:A',13)
        ws.set_column('B:C',18)
        d=cursor.fetchall()
        ws.add_table(0,0,len(d),2,{'columns':columns,'data':d})
        wb.close()

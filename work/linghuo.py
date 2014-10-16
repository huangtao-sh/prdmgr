# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：灵活计息月报导出模块
# 作者：黄涛
# 创建：2014-04-17
from work.basefrm import TrFrame
from xlsxwriter import *
class Linghuo(TrFrame):
    def init(self):
        self['months']=self.create_month_list()
        self.proc_name='linghuorpt'
        self.param_list='month,result'

    def proc_result(self,cursor):
        wb=Workbook('灵活计息月报%s.xlsx'\
                %(self['month']))
        ws=wb.add_worksheet('灵活计息月报')
        num=wb.add_format({'num_format':'0',
            'border':1})
        percent=wb.add_format({'num_format':'0.00%','border':1})
        jine=wb.add_format({'num_format':'#,##0.00;-#,##0.00','border':1})
        border=wb.add_format({'border':1})
        columns=[
                {'header':'分行名称','format':border},
                {'header':'本月笔数','format':num},
                {'header':'笔数同比','format':num},
                {'header':'笔数增幅','format':percent},
                {'header':'本月金额','format':jine},
                {'header':'金额同比','format':jine},
                {'header':'金额增幅','format':percent}]
        ws.set_column(0,0,14)
        ws.set_column(4,5,14)
        d=cursor.fetchall()
        ws.add_table(0,0,len(d),len(columns)-1,{'columns':columns,'data':d})
        wb.close()

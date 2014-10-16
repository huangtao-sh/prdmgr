# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：银企对账报表
# 作者：黄涛
# 创建：2013-7-10
# 修改：2013-8-11 从TrFrame继承
# 修改：2014-02-24 使用QT处理
from .basefrm import TransFrame,TrFrame
from datetime import date
class YinQi(TrFrame):

    def init(self):
        self['months']=self.create_quarter_list()
        self.proc_name='yinqishuju' 
        self.param_list='zhangqi,zdfc,qtfc,zdsh,qtsh,result'
    
    def success(self):
        zdfc,qtfc,zdsh,qtsh=self['zdfc,qtfc,zdsh,qtsh']
        self['report']='银企对账评估报告\n'\
                    '银企对账应对账户数:{0}\n'\
                    '重点账户回收率为:{1:.2f}％\n'\
                    '一般账户为:{2:.2f}％\n'\
                    '银行业金融机构案件防控情况统计表\n'\
                    '上上季应对账户数:{0}\n'\
                    '超过半年未能有效对账户数:{3}\n'\
                    '高管数据报送\n'\
                    '银企对账回收率:{4:.2f}%'\
                    .format(zdfc+qtfc,zdsh/zdfc*100,\
                    qtsh/qtfc*100,zdfc+qtfc-zdsh-qtsh,
                    (zdsh+qtsh)/(zdfc+qtfc)*100) 
        self.treport.copy()

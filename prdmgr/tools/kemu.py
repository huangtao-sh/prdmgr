# Copyrght(C) 2015 Huangtao
# 项目：营运管理平台
# 模块：查询会计科目
# 作者：黄涛
# 创建：2015-2-8
from work.basefrm import TrFrame
class Kemu(TrFrame):
    def init(self):
        super().init()
        self.edtsearch.setFocus()
        
    def search(self):
        if self['search']:
            s='%%%s%%'%(self['search'])
            self['result']=self.query('select item,name from kemu'\
                     ' where item like %s or name like %s',
                         [s,s]).fetchall()
            self.tw.setCurrentCell(0,0)

    def copy(self):
        self.dsc.selectAll()
        self.dsc.copy()
        
    def showdetail(self):
        tw=self.tw
        r=tw.currentRow()
        item=tw.item(r,0).text()
        name=tw.item(r,1).text()
        desc=self.query_str('select describ from kemu where item=%s',
                            (item,))
        self['describ']='<h1>%s\t%s</h1><p>%s</p>'%(item,name,
                    "</p><p>".join(desc.split()))


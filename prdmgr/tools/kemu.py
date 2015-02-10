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
from qtgui.textparser import element,sub_element
class KemuView(TrFrame):
    def init(self):
        self.connect(host='localhost',user='hunter',passwd='123456',
                   db='prdmgr')
        s=['资产类','负债类','所有者权益','资产负债共同类','损益类',
           '或有事项','备查登记类']
        d=element('Root')
        [sub_element(d,x) for x in s]
        categorys=d.childs()
        for r in self.query('select item,name from kemu').fetchall():
            if len(r[0])==4:
                kemu=sub_element(categorys[int(r[0][0])-1],
                    'item',{'text':r})
            else:
                sub_element(kemu,'item',{'text':r})
        self['data']=d
    def click(self,item):
        kemu=item.text(0)
        name=item.text(1)
        desc=self.query_str('select describ from kemu where item=%s',
                            [kemu,])
        if desc:
            self['detail']="<h1>%s\t%s</h1><p>%s</p>"%(kemu,name,
                "</p></>".join(desc.split()))

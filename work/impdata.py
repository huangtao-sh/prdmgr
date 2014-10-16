# 项目：营运管理平台
# 模块：数据导入模块
# 作者：黄涛
# 创建：2013-6-19
# 修订：2013-12-04 新增银企对账签约率数据导入
# 修订：2014-02-24 采用QT界面 
from work.basefrm import TransFrame
from xlrd3 import *
import os
from mylib.my import Mysql

class ImportBase:

    def process(self,filename):
        self.rows=0
        try:
            self.openfile(filename)
            d=[]
            for self.curline in range(self.rows):
                a=self.getline()
                if a:
                    d.append(a)
        finally:
            self.closefile()
        return d
    
    def openfile(self,filename):
        pass
    
    def getline(self):
        return False
    
    def closefile(self):
        pass

class ImportExcel(ImportBase):

    def value(self,i):
        cell=self.ws.cell(self.curline,i)
        if cell.ctype in(1,2):
            v=cell.value
        elif cell.ctype==3:
            if cell.has_date:
                v=cell.date()
            else:
                v=cell.time()
        else:
            v=None
        if v:
            return v
    
    def openfile(self,filename):
        self.onopen()
        self.wb=open_workbook(filename)
        self.ws=self.wb.sheet_by_name(self.sheetname)
        self.rows=self.ws.nrows
    
    def onopen(self):
        pass

class kqzh(ImportExcel,Mysql):

    asql='select Entertime,ExitTime from attendance '\
        'where id=%s and date=%s'

    def onopen(self):
        self.sheetname='第一页'
        self.sql='replace into attendance '\
            'values(%s,%s,%s,%s,%s,%s,%s,Null)'

    def getline(self):
        if self.value(2).isdigit():
            d=[self.value(i) for i in range(2,9)]
            d[0]=d[0].zfill(5)
            kq=self.query_list(self.asql,params=(d[0],d[2]),direction=1)
            if kq:
                enter,exit=kq
                if enter:
                    enter=str(enter).zfill(8)
                    if(d[3] is None)or(enter<d[3].__str__()):
                        d[3]=enter
                if exit:
                    exit=str(exit).zfill(8)
                    if(d[4] is None)or(exit>d[4].__str__()):
                        d[4]=exit
            return d

    def closefile(self):
        pass

class kqkzx(ImportExcel):

    def onopen(self):
        self.sheetname='考勤'
        self.sql='replace into attendance(id,name,date,EnterTime,ExitTime)'\
                ' values(%s,%s,%s,%s,%s)'
    
    def getline(self):        
        a=self.value(0)
        if isinstance(a,float):
            a=str(int(a))
        if a.isdigit():
            d=[a.zfill(5)]
            for i in (1,3,4,5):
                d.append(self.value(i))
            return d

class fhxl(ImportExcel):

    def onopen(self):
        self.sheetname='Sheet1'
        self.sql='update branch set brorder=%s where BranchNo=%s'
    
    def getline(self):
        a=self.value(2)
        if isinstance(a,float):
            a=str(int(a))
        if a and a.isdigit():
            brno="{0:6.0f}".format(self.value(2))
            if brno[3:6]=='999':
                return [int(self.value(0)),brno]

class yjkmm(ImportBase):

    def process(self,filename):
        d=[]
        self.sql='replace into sigcard(No,CardNo,Pwd) values(%s,%s,%s)'
        with open(filename,'r') as fn:
            for r in fn:
                k=r.split()
                if(len(k)==3)and(k[1].isdigit()):
                    d.append(k)
        return d

class kjls(ImportBase):

    def process(self,filename):
        d=[]
        self.sql='replace into cmttrfv values(%s,%s,%s,%s,%s,%s,%s,%s,%s,'\
                '%s,%s,%s)'
        with open(filename,'r') as fn:
            for r in fn:
                k=r.split(',')
                if len(k)>=12:
                    k[3]+=k[4]
                    k.pop(4)
                    d.append(k)
        print(d)
        return d


class yqdz(ImportExcel):

    BRANCH={
    "交通银行安徽省分行":"341999",
    "交通银行北京市分行":"110999",
    "交通银行大连分行":"212999",
    "交通银行福建省分行":"351999",
    "交通银行甘肃省分行":"621999",
    "交通银行广东省分行":"441999",
    "交通银行广西区分行":"451999",
    "交通银行贵州省分行":"521999",
    "交通银行海南省分行":"461999",
    "交通银行河北省分行":"131999",
    "交通银行河南省分行":"411999",
    "交通银行黑龙江省分行":"231999",
    "交通银行湖北省分行":"421999",
    "交通银行湖南省分行":"431999",
    "交通银行吉林省分行":"221999",
    "交通银行江苏省分行":"320999",
    "交通银行江西省分行":"361999",
    "交通银行辽宁省分行":"211999",
    "交通银行内蒙古区分行":"151999",
    "交通银行宁波分行":"332999",
    "交通银行宁夏区分行":"641999",
    "交通银行青岛分行":"372999",
    "交通银行青海省分行":"631999",
    "交通银行厦门分行":"352999",
    "交通银行山东省分行":"371999",
    "交通银行山西省分行":"141999",
    "交通银行陕西省分行":"611999",
    "交通银行上海市分行":"310999",
    "交通银行深圳分行":"443999",
    "交通银行四川省分行":"511999",
    "交通银行苏州分行":"325999",
    "交通银行天津市分行":"120999",
    "交通银行无锡分行":"322999",
    "交通银行云南省分行":"531999",
    "交通银行浙江省分行":"331999",
    "交通银行新疆维吾尔自治区分行":"651999",
    "交通银行重庆市分行":"500999"}
    
    def onopen(self):
        self.sheetname='企银对账统计表'
        self.sql='replace into yinqiduizhang '\
        'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    def openfile(self,filename):
        super().openfile(filename)
        self.zq=os.path.basename(filename)[7:13]
    
    def getline(self):
        s=[self.zq]
        brname=self.value(0)
        if brname in self.BRANCH:
            s.append(self.BRANCH[brname])
            for i in (1,2,3,4,7,8,11,12,13,14,15,16,17,18,21,0):
                s.append(self.value(i))
            return s

class yycp(ImportExcel):

    def process(self,filename):
        self.rows=0
        try:
            self.openfile(filename)
            d=[]
            for self.curline in range(self.rows):
                a=self.getline()
                if a:
                    d.append(a)
        finally:
            self.closefile()
        return d

    def onopen(self):
        self.sql='replace into productcode (bankuai,level1,'\
                'level2,level3,level4,level5,productno,shiyong,'\
                'executename,describ,subject, subname,type,xuqiu)'\
                'values(%s,%s,%s,%s,%s,%s,%s,'\
                '%s,%s,%s,%s,%s,%s,%s)'        
    
    def getline(self):        
        a=self.value(0)
        if isinstance(a,float):
            a=str(int(a))
        if a.isdigit():
            d=[a.zfill(5)]
            for i in (1,3,4,5):
                d.append(self.value(i))
            return d

class fhlxr(ImportExcel):

    def onopen(self):
        self.sheetname='Sheet1'
        self.sql='replace into yewulianxiren '\
        'values(%s,%s,%s,%s,%s)'
        self.prev=[None,None,None,None,None]
    def openfile(self,filename):
        super().openfile(filename)
        self.fh=os.path.basename(filename)[0:2]
    
    def getline(self):
        s=[self.fh]
        yw=self.value(1)
        if yw and(yw!='工作内容'):
            s.append(yw)
            for i in (2,3,4):
                v=self.value(i)
                if not v:
                    v=self.prev[i]
            self.prev=s
            return s

class Yinqi(ImportExcel):
    def onopen(self):
        self.sheetname='电子对账签约情况表'
        self.sql='replace into yinqiqianyue '\
                'values(%s,%s,%s,%s,%s,%s)'
    def openfile(self,filename):
        super().openfile(filename)
        self.date=os.path.basename(filename)[8:14]
    def getline(self):
         brno=self.value(1)
         if brno and(len(brno)==11):
             brno=brno[2:8]
             s=[self.date,brno,self.value(3),self.value(4),\
                     self.value(6),self.value(7)]
             return s

class linghuo(ImportExcel):
    CCY={
            '人民币':'CNY',
            '美元':'USD',
            '港币':'HKD',
            '欧元':'EUR',
        }
    def onopen(self):
        self.sheetname='灵活计息业务量统计表'
        self.sql='replace into linghuo '\
                'values(%s,%s,%s,%s,%s,%s)'
    def openfile(self,filename):
        super().openfile(filename)
        self.date=os.path.basename(filename)[-11:-4]
    def getline(self):
        brno=self.value(0)
        if brno:
            if len(brno)==11:
                brno=brno[2:8]
            elif len(brno)==6:
                pass
            else:
                return
            s=[self.date,brno,self.CCY[self.value(2)],
                    self.value(3),self.value(4),self.value(5)]
            return s

class Import(TransFrame):

    IMPORTTYPE={
            '01-考勤数据（总行）':kqzh,
            '02-考勤数据（卡中心）':kqkzx,
            '03-印鉴卡密码':yjkmm,
            '04-银企对账数据':yqdz,
            '05-省直分行序列':fhxl,
            '06-营运产品码':yycp,
            '07-分行联系人':fhlxr,
            '08-电子对账签约率':Yinqi,
            '09-会计流水':kjls,
            '10-灵活计息':linghuo,
            }

    def init(self):
        self['imptypes']=sorted(list(self.IMPORTTYPE))

    def submit(self):
        initial_path=self.initial_path(self['imptype'][3:])
        files=self.get_open_files(
                '打开导入文件',
                initial_path ,
                "Files (*.txt;*.xls)"
               ) 
        if files:
            imp=self.IMPORTTYPE[self['imptype']]()
            for file_name in files:
                d=imp.process(file_name)
                if d:
                    self.notify('%s 文件正在导入'%(file_name))
                    self.texec(imp.sql,d)
                    affrows=len(d)
                    self.notify('%s 条记录被导入'%(affrows))
                    n=os.path.basename(file_name)
                    self.reg_journal('Import','类型：%s,文件名：%s,数量:%s'\
                            %(str(self['imptype'][2:]),n,affrows))
            self.showinfo('处理结束')
            p=os.path.dirname(files[0])
            self.initial_path(str(self['imptype'][3:]),p)
             

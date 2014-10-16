# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：导出印鉴卡密码模块
# 作者：黄涛
# 创建：2013-6-29

from .basefrm import TransFrame
class SigExport(TransFrame):

    sql="select CardNo,Pwd from SigCard where CardNo"\
            " between %s and %s order by CardNo"
    
    initpath='D:/huangtao/Documents/工作平台/业务报表/防伪系统文件/下发/'
    
    def init(self):
        self['Encrypt']='1'
        self.branch_list['values']=" ".join(\
            self.query_list('select BranchName from branch '\
            'where Level in(1,2) order by brorder'))
    
    def process(self,cur):
        filename=self.initpath+'%s-(%s-%s).dat'%(self.fh,self.b,self.e)
        with open(filename,'w') as f:    
            f.write('\n\n')
            if self['Encrypt']=='1':
                for CardNo,Pwd in cur:
                    f.write("           %s=     %s=\n"\
                            %(encrypt(CardNo),encrypt(Pwd)))
            else:
                for CardNo,Pwd in cur:
                    f.write("%s%s\n"%(CardNo,Pwd))
        self.aff_rows=cur.rowcount
            
    def submit(self):
        self.b=self['beginno'].zfill(8)
        self.e=self['endno'].zfill(8)
        self.fh=self['branch']
        if self.e<self.b:
            self.showerr('起始号码应大于终止号码！')
            return 
        self.query(self.sql,params=(self.b,self.e),proc=self.process)
        self.reg_journal('ExportSigcard','分行：%s;%s-%s'\
                    %(self.fh,self.b,self.e))    
        self.notify('导出成功，记录数：%s'%(self.aff_rows))
        self.showinfo('导出成功!')

def encryp(CardNo):
    '''
    此代码比较少，但执行效率没有下面函数好
    '''
    Key=(('MD','MT','Mj','Mz','ND','NT','Nj','Nz','OD','OT'),
        'AEIMQUYcgk','wxyz012345')
    s=[ord(x)-48 for x in CardNo.zfill(8)]
    return "".join([Key[i % 3][s[i]] for i in range(8)])

def encrypt(CardNo):
    '''
    金联安公司印鉴卡加密函数
    调用方法：s=encrypt(CardNo)
    '''
    Key=(('MD','MT','Mj','Mz','ND','NT','Nj','Nz','OD','OT'),
        'AEIMQUYcgk','wxyz012345')
    CardNo=CardNo.zfill(8)
    r=''
    k=0
    for c in CardNo:
        t=ord(c)-48
        r=r+Key[k][t]
        k=k+1
        if k==3:k=0
    return r

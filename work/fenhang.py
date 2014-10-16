# 项目：营运管理平台
# 模块：分行序列
# 作者：黄涛
# 创建：2013-7-16
# 修订：2014-2-24 修改为QT交易界面

from work.basefrm import TransFrame
class Fenhang(TransFrame):

    def init(self):
        self.query('select branchname,`order` from report_branch'\
                " where(level in(1,2))and(branchno<'800000')"\
                ,proc=self.proc)

    def submit(self):
        s=self['brs']
        if s is None:return
        seps='、，, \n\t'
        d=self.split_str(s,seps)
        result={}
        for i in d:
            for k in self.d:
                if k.find(i)>=0:
                    result[self.d[k]]=k
        r="、".join([result[x] for x in sorted(result.keys())])
        self['ordersbrs']=r

    def proc(self,cursor):
        if cursor:
            self.d={brname:order for brname,order in cursor}

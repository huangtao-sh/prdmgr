# Copyrght(C) 2014 Huangtao
# 项目：营运管理平台
# 模块：计算素数
# 作者：黄涛
# 创建：2014-08-05
from work.basefrm import TrFrame
class SuShu(TrFrame):

    initial={'max':500,}
    def submit(self):
        result=[]
        for i in range(2,self['max']):
            if all([i % x for x in result]):
                result.append(i)
        s=[str(x) for x in result]
        self['result']=','.join(s)
        
class GongYue(TrFrame):

    def submit(self):
        def gcd(a,b):
            if a<b:
                a,b=b,a
            while b:
                a,b=b,a%b
            return a
        a,b=self['a,b']
        self['gcd,gbs']=gcd(a,b),a*b//gcd(a,b)
        

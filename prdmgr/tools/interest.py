# 项目：营运管理平台
# 模块：计算利息
# 作者：黄涛
# 创建：2014-7-18

from work.basefrm import TransFrame
from datetime import date,datetime
from mylib.stdlib import year_frac,date_add

class Interest(TransFrame):
    BASIS={
        '0-30/360':0,
        '1-ACT/365':1,
        '2-ACT/360':2,
        '3-AFI/365':3,
        '4-30E/360':4,
        '5-对年对月对日':5,
        }
    initial={
            'start_date':date.today(),
            'end_date':date_add(date.today(),years=1),
            'amount':10000,
            'rate':2.0,
            'basis_items':sorted(BASIS.keys())
            }

    def submit(self):
        begin=self['start_date']
        end=self['end_date']
        basis=self.BASIS[self['basis']]
        days,frac=year_frac(begin,end,basis)
        rate=self['rate']/100
        amount=self['amount']
        self['days']=days
        self['interest']=round(amount*rate*frac,2)

    def change(self):
        try:
            self.submit()
        except:
            pass

        

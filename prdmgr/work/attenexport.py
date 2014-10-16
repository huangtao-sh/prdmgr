# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：关于模块
# 作者：黄涛
# 创建：2013-7-3
# 修改：2013-8-28 修改为使用win32py的COM接口导出Excel文件
# 修改：2013-11-26 候改为导出文本文件，由文本文件再导入Excel
# 修改：2014-02-24 修改为QT处理
# 修改：2014-02-26 采用Spinbox控件
from .basefrm import TransFrame
from datetime import date,time,timedelta
from calendar import *
class AttendanceExport(TransFrame):
    zts_sql="select count(id) from attendance where `date` like %s"\
            " and  id='01974'"
    gzts_sql='select count(id) from attendance where `date` like %s '\
            "and  id='01974' and(Memo<>'非工作日' or Memo is null)"
    renyuanxinxi='select * from renyuanxinxi order by listorder'
    jiaqi_sql="select `date` from attendance where id='01974'"\
            " and memo='非工作日' and date like %s"
    file_name='D:/huangtao/Documents/工作平台/业务报表/考勤报送/'\
            'attendance.txt'
    gt_dtl_sql='select date,entertime,ExitTime from attendance '\
            'where id =%s and date like %s'

    def init(self):
        self['months']=self.create_month_list()

    def submit(self):
        ren_yuan=self.query_data(self.renyuanxinxi)
        jia_qi=[x[0] for x in self.query_data(self.jiaqi_sql,
                params=(self.cur_month+'%',))]
        jbmx,jbhz,jdkq,zjbt=[],[],[],[]
        zhry=0
        yf="%s年%s月份"%(self.cur_month[0:4],self.cur_month[5:7])
        for r in ren_yuan:
            dtl=self.query_data(self.gt_dtl_sql,params=(r[0],
                self.cur_month+'%'))
            d=list(r[1:9])
            d[6]=str(d[6])
            d[7]=str(d[7])
            jbhz.append(d)
            wd=0
            jb=[]
            if r[1]=='1001':
                zfbz='总行'
            else:
                zfbz='分行借调'
            kq=[r[6],r[13],zfbz,jb]
            for dt,et,xt in dtl:
                if dt in jia_qi:
                    if et and xt:
                        jb.append([dt,str(et),str(xt)])
                else:
                    if et or xt:
                        if xt is None:
                            xt=et
                        if xt.seconds>=64800:
                            jb.append([dt,'18:00:00',str(xt)])
                        wd+=1
            jbmx.append(kq)
            if r[1]=='1001':
                zhry+=1
                zh=[zhry,r[5],r[6]]
                zh+=r[9:13]
                if wd>=int(self['zhts']):
                    zh.append('满勤')
                else:
                    zh.append('%d天'%wd)
                zh.append(700)
                zjbt.append(zh)
            else:
                fh=list(d)
                wd=wd+int(self['zts'])-int(self['fhts'])
                if wd>=int(self['zts']):
                    fh.append('31天')
                else:
                    fh.append('%d天'%wd)
                if r[1]=='1023':
                    fh.append('否')
                else:
                    fh.append('是')
                jdkq.append(fh)
                    
        with open(self.file_name,'w') as fn:
            fn.write('加班情况表\n')
            for row in jbhz:
                fn.write('%s,%s,%s,%s,%s,%s,%s,%s\n'%tuple(row))
            fn.write('531工程人员加班明细表\n')
            for row in jbmx:
                if row[1]=='C':
                    zd='C职等'
                else:
                    zd='AB职等'
                fn.write('%s,%s,%s\n'%(row[0],row[2],zd))
                for r in row[3]:
                    fn.write('%s,%s,%s\n'%tuple(r))
            fn.write('借调人员考勤表\n')
            for row in jdkq:
                fn.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%tuple(row))
            fn.write('总行人员张江交通补贴表\n')
            for row in zjbt:
                fn.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%tuple(row))
            self.showinfo('导出成功') 

        '''
        xls=Excel(self.filename%(self.cur_month))
        try:
            xls.sheetname='加班情况汇总表'
            xls.set_value(1,1,'531工程人员加班情况汇总表--%s'%(yf)) 
            rn=4
            for row in jbhz:
                ln=1
                for c in row:
                    xls.set_value(rn,ln,c)
                    ln+=1
                rn+=1

            xls.sheetname='531工程人员加班明细表'
            xls.set_value(1,1,'531工程人员加班情况明细表--%s'%(yf)) 
            i=0
            for row in jbmx:
                xls.set_value(4,i*3+5,i+1)
                xls.set_value(6,i*3+5,row[0])
                if row[1]=='C':
                    zd='C职等'
                else:
                    zd='AB职等'
                xls.set_value(7,i*3+5,row[2])
                xls.set_value(8,i*3+5,zd)
                for dt,et,xt in row[3]:
                    rn=dt.day+9
                    ln=i*3+5
                    xls.set_value(rn,ln,et)
                    xls.set_value(rn,ln+1,xt)
                i+=1
            xls.sheetname='借调人员考勤表'
            xls.set_value(1,1,'借调人员考勤表--%s'%(yf)) 
            rn=6
            for row in jdkq:
                ln=1
                for c in row:
                    xls.set_value(rn,ln,c)
                    ln+=1
                rn+=1
            
            xls.sheetname='总行人员张江交通补贴表'
            xls.set_value(2,1,'531工程总行人员张江交通补贴 -- %s'%(yf)) 
            rn=6
            for row in zjbt:
                ln=1
                for c in row:
                    xls.set_value(rn,ln,c)
                    ln+=1
                rn+=1 
        finally:
            xls.save()
            xls.quit()
        self.showinfo('导出成功')
    '''

    @property
    def cur_month(self):
        return self['month']

    def select_month(self):
        self['zts']=str(\
                self.query_str(self.zts_sql,(self.cur_month+'%',)))
        self['fhts']=\
                self.query_str(self.gzts_sql,(self.cur_month+'%'\
                        ,))
        self['zhts']=self['fhts']

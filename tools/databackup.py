# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：数据库备份恢复模块
# 作者：黄涛
# 创建：2014-7-23
from work.basefrm import TrFrame
from os import listdir,system
from os.path import join,isfile
from datetime import date
class DataBackup(TrFrame):
    initial={'func_items':'0-备份 1-恢复'.split()}
    
    def submit(self):
        m=self.my_cnf()
        security='-u%s -p%s %s'%(m['user'],m['passwd'],m['db'])
        fn=join(self.path,self['file_name'])
        self.notify('选择文件%s'%(fn))
        if not self['func']:
            cmd='mysqldump %s -R | gzip > %s '%(security,fn)
        else:
            cmd='gzip -d < %s | mysql %s'%(fn,security)
        self.notify('开始执行命令：%s '%(cmd))
        system(cmd)
        self.notify('执行命令成功！')

    def func_change(self):
        path=join(self.base_dir,'data')
        self.path=path
        files=[f for f in listdir(path) if isfile(join(path,f))]
        if not self['func']:
            fn='prdmgr%s.gz'%(date.today())
            if fn not in files:
                files.append(fn)
        self['files']=sorted(files,reverse=True)



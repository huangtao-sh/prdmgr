# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：关于模块
# 作者：黄涛
# 创建：2013-7-2
# 修改：2014-2-14 采用QT模式处理
# 修改：2014-7-23 采用HTML编写界面
#from .basefrm import TransFrame
from mylib.qtgui import BaseForm
class About(BaseForm):
    initial={'msgvar':'''
        <center>
        <br/><br/>
        营运管理平台Ver 1.0<br/><br/>
        作者：黄涛<br/><br/>
        创建：2013-7-2<br/><br/>
        电子邮件：<a href='mailto:huangtao.jh@gmail.com'>huangtao.jh@gmail.com</a><br/><br/>
        </center>
        ''',
        }

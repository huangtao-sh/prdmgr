# Copyrght(C) 2013 Huangtao
# 项目：营运管理平台
# 模块：身份证校验位计算
# 作者：黄涛
# 创建：2013-7-28

from .basefrm import TransFrame
class IdCard(TransFrame):
    def submit(self):
        cardno=get_checksum(self['idcard'])
        if cardno:
            self['idcard']=cardno

def get_checksum(id_number):
    '''
    身份证校验位计算
    输入15位或18位身份证号码
    返回带校验位正确的身份证号码
    '''
    xishu=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
    check=('10X98765432')
    checksum=0
    length=len(id_number)
    if 15==length:
        id_number=id_number[0:6]+'19'+id_number[6:]
        length+=2
    if 18>=length>=17:
        for i in range(17):
            checksum+=(ord(id_number[i])-48)*xishu[i]
        return id_number[:17]+check[checksum%11]
         

import mysql.connector
import cProfile

def Encrypt(CardNo):
    Key1='MNO'
    Key2='DTjz'
    Key3='AEIMQUYcgk'
    Key4='wxyz012345'
    No=CardNo.zfill(8)
    k=1
    r=''
    for c in No:
        t=ord(c)-48
        if k==1:
            r=r+Key1[(t//4)]
            r=r+Key2[t % 4]
        elif k==2:
            r=r+Key3[t % 10]
        else:
            r=r+Key4[t % 10]    
            k=0
        k=k+1
    return r


print('印鉴卡密码导出程序 1.0')
fh=input('请输入分行名称:')
b=input('请输入起始号码：').zfill(8)
e=input('请输入终止号码：').zfill(8)
Confirm=input('分行号名称：%s,起始号码：%s，终止号码：%s，是否确认Y or N？'%(fh,b,e))


if Confirm=='y':
    my=mysql.connector.connect(host='localhost',user='hunter',passwd='123456',db='prdmgr')
    cur=my.cursor()
    sql="select CardNo,Pwd from SigCard where CardNo between %s and %s order by CardNo"
    cur.execute(sql,(b,e))
    with open('%s-(%s-%s).dat'%(fh,b,e),'w') as f:    
        f.write('\n\n')
        for CardNo,Pwd in cur:
            f.write("       %s=     %s=\n"%(Encrypt(CardNo),Encrypt(Pwd)))
    cur.close()
    my.close()

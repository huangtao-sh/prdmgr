import smtplib
from email.mime.text import MIMEText  
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders
import os.path
class EMail:
    def __init__(self):
        self._Subject=''
        self._From='huangtao@bankcomm.com'
        self._To=[]
        self._Cc=[]
        self.Content=[]
    def AddText(self,text):
        msg=MIMEText(text,'plain','utf-8')
        self.Content.append(msg)
    def AddHtml(self,text):
        msg=MIMEText(text,'html','utf-8')
        self.Content.append(msg)
    def AddAttr(self,filename):
        with open(filename,'rb') as fn:
            ctype,encoding=mimetypes.guess_type(filename)
            if ctype is None or encoding is not None:
                ctype='application/octet-stream'
            maintype,subtype=ctype.split('/',1)
            msg = MIMEBase(maintype,subtype,charset='utf-8')
            msg.set_payload(fn.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition','attachment;filename="%s"'%os.path.basename(filename))
#            msg['Content-Disposition']='attachment;filename=%s'%(fm)
            self.Content.append(msg)
    def Send(self):
        smtp=smtplib.SMTP('smtp.bankcomm.com')
        smtp.login('huangtao','Huangtao1415')
        smtp.sendmail(self.From,tuple(self.To+self.Cc),self.String)
        smtp.quit()
    @property
    def From(self):
        return self._From
    @property
    def To(self):
        return self._To
    @To.setter
    def To(self,to):
        self._To=to
    @property
    def Cc(self):
        return self._Cc
    @Cc.setter
    def Cc(self,cc):
        self._Cc=cc
    @property
    def Subject(self):
        return self._Subject
    @Subject.setter
    def Subject(self,subject):
        self._Subject=subject
    def Save(self,filename):
        with open(filename,'w',encoding='utf-8') as fn:
            fn.write(self.String)
    @property
    def String(self):
        if len(self.Content)==0:
            return
        elif len(self.Content)==1:
            msg=self.Content[0]
        else:
            msg=MIMEMultipart()
            for m in self.Content:
                msg.attach(m)
        msg['Subject']=self.Subject
        msg['From']=self.From
        msg['To']=';'.join(self.To)
        msg['Cc']=';'.join(self.Cc)
        return msg.as_string()
'''
mail=EMail()
mail.Subject='邮件测试'
mail.To=["'黄涛'<huangtao@bankcomm.com>",'hunto@163.com']
mail.Cc=['huangtao.jh@gmail.com']
#mail.AddText('邮件测试，这是一个邮件测试')
mail.AddHtml('<html><b>粗体测试</b><p>中国人不打中国人</html>')
mail.AddAttr('d:/test.txt')
mail.AddAttr('d:/1.jpg')
mail.AddAttr('D:/huangtao/Pictures/妈妈.jpg')
mail.AddAttr(r'D:\huangtao\Dropbox\Python\WorkMgr\资料\tkinter中文.pdf')
mail.Save('d:/a.eml')
'''

import smtplib
from email.message import EmailMessage

class Email_SMTP():
    def __init__(self,sender_site,sender,password,receiver,subject='',body_plaintext='', body_HTML='',attachment=''):
        self.sender = sender
        self.password = password
        self.receiver = receiver # może być str, ale także lista
        self.subject = subject
        self.body_plaintext = body_plaintext
        self.body_HTML = body_HTML
        self.attachment = attachment
        
        self.sender_site = sender_site
        match self.sender_site:
            case "test":
                self.host = 'localhost'
                #self.port = '1025'
            case "gmail":
                self.host = 'smtp.gmail.com'
                #self.port = '587'
            case "interia":
                self.host = 'poczta.interia.pl'
                #self.port = '587' #SSL - 465
        
    def Send_email_SMTP(self):
        port = '587'
        with smtplib.SMTP(self.host, port) as smtp:
            
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            
            smtp.login(self.sender,self.password)
            msg = f"Subject: {self.subject}\n\n{self.body_plaintext}"
            smtp.sendmail(sender,receiver,msg)
    
    def Send_email_SMPT_SSL(self):
        port='465'
        
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg.set_content = self.body_plaintext
        msg.add_alternative(self.body_HTML,'html') #zweryfikować bo self.body_HTML ma być w potrójnym cudzysłowiu
        
        for attachment in self.attachment:
            with open(attachment,'rb') as f:
                attachment_data = f.read()
                attachment_name = f.name
            msg.add_attachment(attachment_data,maintype ='application', subtype='octet-stream',filename = attachment_name)
            
        with smtplib.SMTP_SSL(self.host, port) as smtp:
            smtp.login(self.sender,self.password)
            smtp.send_message(msg)
# TEST: 
# config email details
sender_site = 'gmail'
sender = 'g.pardela1@gmail.com'
password = 'Dnieje_1'
receiver = 'g.pardela1@gmail.com'
receiver = ['g.pardela1@gmail.com','g.pardela@interia.pl']
subject = 'test1'
body_plaintext = 'test_body'

with open('h.html','r') as f:
    rhtml = f.read()
    
bodyHTML= rhtml
attachment = ['emailtest1.txt','requirements.txt']

m = Email_SMTP(sender_site,sender,password,receiver,subject,body_plaintext,bodyHTML,attachment)
m.Send_email_SMPT_SSL()

print('test')
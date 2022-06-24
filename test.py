import imaplib

imaplib.IMAP4_SSL
 
mail = imaplib.IMAP4_SSL("imap-mail.outlook.com",993)
mail.login('sandysansy@outlook.cl', '3bahos36')
mail.list()
mail.select('inbox')
 
#need to add some stuff in here

mail.logout()
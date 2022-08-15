import smtplib
from sqlite3 import connect

my_email = "stevenswynter@gmail.com"
password = "cybercrea"



connexion = smtplib.SMTP("smtp.gmail.com") 
connexion.starttls()
connexion.login(user=my_email, password=password)
connexion.sendmail(from_addr=my_email, to_addrs="foplacide@gmail.com", msg="Subject:\n\n This is the body of the email Hello world")
connexion.close()
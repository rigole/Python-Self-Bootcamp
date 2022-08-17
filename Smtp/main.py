""" 
import smtplib
from sqlite3 import connect

my_email = "stevenswynter@gmail.com"
password = "cybercrea"



connexion = smtplib.SMTP("smtp.gmail.com") 
connexion.starttls()
connexion.login(user=my_email, password=password)
connexion.sendmail(from_addr=my_email, to_addrs="foplacide@gmail.com", msg="Subject:\n\n This is the body of the email Hello world")
connexion.close()



import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.weekday()

print(month)

"""

import random
import smtplib
import datetime as dt

MY_EMAIL = "stevenswynter@gmail.com"
MY_PASSWORD = "cybercrea"



now = dt.datetime.now()
week = now.weekday()

if week == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"SUBJECT:Monday Motivation\n\n{quote}"
            )
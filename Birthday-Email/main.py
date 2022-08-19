import datetime as dt
from importlib.resources import contents
import pandas as pd
import random
import smtplib

today = (dt.datetime.now().month, dt.now().day)

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "1234565"
data = pd.read_csv("birthdays.csv")

#birthdays_dict = {
#    (birthday_month, birthday_daty) : data_row
#}

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, row) in data.iterrows()}

if today  in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contens = letter_file.read()
        contens.replace("[NAME]", birthday_person["name"])
        
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
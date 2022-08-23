#from time import time

import requests
from datetime import datetime
import smtplib
import time

my_email = "stevenswynter@gmail.com"
password = "cybercrea"
MY_LAT = 	7.369722
MY_LONG = 12.354722

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()



    iss_longitude = float(data["iss_position"]["longitude"])

    iss_latitude = float(data["iss_position"]["latitude"])

    #iss_position = (longitude, latitude)

    #print(iss_position)


    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
    
 

   
while True:
    
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs=my_email,
            msg="Subject:Look Up\n\n The ISS is above you in the sky."
        )




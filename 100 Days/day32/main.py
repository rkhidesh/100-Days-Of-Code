# from multiprocessing import connection
# import smtplib
# import datetime as dt
# import random

# current_time = dt.datetime.now()
# weekday = current_time.weekday()
# if weekday == 5:
#     with open("100-Days-Of-Code/100 Days/day32/quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

# date_of_birth = dt.datetime(year=2002, month=8, day=23)

# my_email = "rebeccakhidesheli@yahoo.ca"
# password = "hkedvpcvfoxvbrzh"

# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password= password)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday Motivation \n\n {quote}")

##################### Normal Starting Project ######################

import datetime as dt
from importlib.resources import contents
from socket import TCP_NODELAY
import pandas
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)
my_email = "rebeccakhidesheli@yahoo.ca"
password = "hkedvpcvfoxvbrzh"
data = pandas.read_csv("100-Days-Of-Code/100 Days/day32/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"100-Days-Of-Code/100 Days/day32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"] )

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
         connection.starttls()
         connection.login(user=my_email, password= password)
         connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday \n\n {contents}")





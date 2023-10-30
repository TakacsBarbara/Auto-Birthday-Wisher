import datetime as dt
import pandas
import random
import smtplib

my_email = "teszt.barbara.27@gmail.com"
my_password = "pfxk qbmx jaga kren"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        message = f"Subject:Happy Birthday! 💖\n\n{contents}".encode('utf-8')

        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="barbiteszt@yahoo.com",
            msg=message
        )



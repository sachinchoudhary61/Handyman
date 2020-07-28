import smtplib
import datetime
import uuid


def otp_sending():

    stringLength = 6
    randomString = uuid.uuid4().hex  # get a random string in a UUID fromat
    randomString = randomString.upper()[0:stringLength]  # convert it in a uppercase letter and trim to your size.
    return randomString

def time_gen():

    now = datetime.datetime.now()
    x = (now.strftime("%Y-%m-%d"))
    return x




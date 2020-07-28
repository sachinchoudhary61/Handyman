import smtplib , ssl
from django.shortcuts import HttpResponse
def smtp(name,l,otp,email):
    msg = "--*---*------WELCOME TO OUR HandyMan -----*---*--\n\n\n" \
          "          HI,%s \n\n" \
          "          This OTP is confidential." \
          " For security reasons,\n" \
          "           DO NOT share the LINK with anyone. \n\n" \
          "             LINK   : %s \n\n" \
          "          LINK GENERATION TIME      : %s \n\n" % (name, l, str(otp))

    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login('godhelpmetogrow@gmail.com', 'sachu123@')
    # server.sendmail('godhelpmetogrow@gmail.com', email, msg)
    # server.quit()


    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "godhelpmetogrow@gmail.com"
    receiver_email = email
    password = 'sachu123@'

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)

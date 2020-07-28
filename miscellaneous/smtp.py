import smtplib
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
    # ('mail.your-domain.com', 25)
    try:
       smtpObj = smtplib.SMTP('mail.https://guarded-thicket-09826.herokuapp.com', 25)
       smtpObj.sendmail('godhelpmetogrow@gmail.com', email, msg)
    except smtplib.SMTPException:
       return HttpResponse("<h1>Error: unable to send email</h1>")

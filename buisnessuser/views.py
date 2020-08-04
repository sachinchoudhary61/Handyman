from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from miscellaneous.otp_sending import otp_sending, time_gen
from django.core.mail import EmailMessage
from buisnessuser.models import Professional_user


def signup(request):

    global user_image1
    if request.method == "POST":
        user_image = None
        if request.FILES:
            myfile = request.FILES["user_image"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            user_image = fs.url(filename)
            user_image = myfile.name

        form = Professional_user_Form(request.POST)
        f = form.save(commit=False)

        f.user_Img = user_image
        f.first_name = request.POST["first_name"]  # column name
        f.last_name = request.POST["last_name"]
        f.is_active = False
        f.email = request.POST["email_id"]
        p1 = request.POST["password"]
        p2 = request.POST["confirm_password"]
        if p1 == p2:
            f.password = p2
        else:
            return HttpResponse("<h1> Password and confirm Password is not same </h2>")

        f.Contact_no = request.POST["c_number"]
        f.city = request.POST["my_field"]
        f.address = request.POST['address']
        f.otp = otp_sending()
        f.otp_gen_time = time_gen()
        f.account_creation = time_gen()
        f.last_login = time_gen()
        f.is_professional_user = True
        token = f.otp + time_gen()
        link = 'https://guarded-thicket-09826.herokuapp.com/activeness/?token=' + str(token) + '&email=' + f.email
        f.token = token

        name = f.first_name + " " + f.last_name

        msg = "--*---*------WELCOME TO HandyMan -----*---*--\n\n\n" \
              "          HI,%s \n\n" \
              "          This Link is confidential." \
              " For security reasons,\n" \
              "           DO NOT share the LINK with anyone. \n\n" \
              "             LINK   : %s \n\n" \
              "          LINK GENERATION TIME      : %s \n\n" % (name, link, str(f.otp_gen_time))
        email1 = EmailMessage(
            "Account Activation", msg, to=[f.email]
        )
        email1.send()
        f.save()
        return HttpResponse("<h1> VERIFY THE USER , SEE YOUR EMAIL </h1>")
    return render(request, "professional_user/signup.html")


def verifyuser(request):
    token = request.GET["token"]
    email = request.GET["email"]
    data = Professional_user.objects.get(email=email)
    tokenvalue = data.token
    fecthed_id = data.user_id

    if token == tokenvalue:
        update = Professional_user(
            user_id=fecthed_id,
            is_active=True
        )
        update.save(update_fields=["is_active"])

        return render(request, "normaluser/Login.html")

    else:
        return HttpResponse("<h1>not verified </h1>")


def login(request):
    if request.method == "POST":
        username = request.POST["un"]
        up = request.POST["password"]
        try:
            data1 = Professional_user.objects.get(email=username)
        except:
            return render(request, "professional_user/login.html", {'email_error': True})
        dp = data1.password
        active = data1.is_active
        professional_user = data1.is_professional_user

        if not active:
            return render(request, "professional_user/login.html", {'active_error': True})
        else:
            if dp == up:
                request.session['email'] = username
                request.session['Authentication'] = True
                if professional_user is True:
                    return HttpResponse("<h1> Welcome to the Professional user page</h1>")
                else:
                    return HttpResponse("<h1> Normal User page</h1>")
            else:
                return render(request, "login.html", {'password_error': True})
    return render(request, "professional_user/login.html")

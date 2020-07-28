from django.shortcuts import render
from buisnessuser.models import citylist, Professional_user
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
from miscellaneous.otp_sending import otp_sending, time_gen
from miscellaneous.smtp import smtp
import datetime
from buisnessuser.models import Professional_user
def my_view(request, *a, **kw):
    # view logic
    return render(request, "professional_user/p_user_signup.html", choices =citylist())

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

        # f.IMg_name = user_image
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
        f.otp = otp_sending()  # column name
        f.otp_gen_time = time_gen()
        f.account_creation = time_gen()
        f.last_login = time_gen()
        f.is_professional_user = True
        token = f.otp+time_gen()
        link = 'https://guarded-thicket-09826.herokuapp.com/activeness/?token='+str(token)+'&email='+f.email
        f.token = token

        name = f.first_name+" "+f.last_name
        smtp(name, link, f.otp_gen_time, f.email)
        f.save()
        return HttpResponse("<h1> VERIFY THE USER , SEE YOUR EMAIL </h1>")
    return render(request, "professional_user/p_user_signup.html")

def verifyuser(request):

    token = request.GET["token"]
    email = request.GET["email"]
    data = Professional_user.objects.get(email=email)
    print(data)
    tokenvalue = data.token
    id = data.id
    print(tokenvalue)

    if (token == tokenvalue ):
        update = Professional_user(
            user_id=id,
            is_active=True
        )
        update.save(update_fields=["is_active"])

        return render(request, "normaluser/Login.html")

    else:
       return HttpResponse("<h1>not verified </h1>")

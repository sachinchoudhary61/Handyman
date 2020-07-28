from django import forms
from buisnessuser.models import Professional_user
class Professional_user_Form(forms.ModelForm):
    class Meta():
        model= Professional_user
        #fields = '__all_' # automatically

        exclude = ["first_name", "last_name", "is_active", "email", "password",
                   "Contact_no", "city", "address", "otp",
                   "otp_gen_time", "token", "account_creation",
                   'last_login', 'user_Img', 'is_professional_user']
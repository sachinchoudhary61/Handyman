from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Professional_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    email = models.CharField(unique=True, default="", max_length=200)
    password = models.CharField(max_length=50)
    Contact_no = PhoneNumberField(null=False, blank=False, unique=True)
    service_level_choice = [
        ('AGRA', 'Agra'), ('AHMEDABAD','Ahmedabad'), ('ALAPPUZHA', 'Alappuzha'), ('ALWAR', 'Alwar'), ('AMRITSAR', 'Amritsar'), ('AURANGABAD', 'Aurangabad'), ('BANGALORE', 'Bangalore'), ('BHARATPUR', 'Bharatpur'), ('BHAVANAGAR','Bhavnagar'),
        ('BHIKANER','Bhikaner'), ('BHOPAL', 'Bhopal'), ('BHUBANESHWAR', 'Bhubaneshwar'), ('BODH GAYA','Bodh Gaya'), ('CALANGUTE','Calangute'), ('CHANDIGARH', 'Chandigarh'), ('CHENNAI', 'Chennai'), ('CHITTAURGARH', 'Chittaurgarh'),
        ('COIMBATHORE', 'Coimbatore'), ('CUTTACK', 'Cuttack'), ('DALHOUSIE', 'Dalhousie'), ('DEHRADUN', 'Dehradun'), ('DELHI','Delhi'), ('DIU_ISLAND', 'Diu - Island'), ('ERNAKULAM', 'Ernakulam'), ('FARIDABAD', 'Faridabad'), ('GAYA', 'Gaya'), ('GANGTOK', 'Gangtok'), ('GHAZIBAD', 'Ghaziabad'),
        ('GURGAON','Gurgaon'), ('GUWAHATI','Guwahati'), ('GWALIOR', 'Gwalior'), ('HARIDWAR', 'Haridwar'), ('HYDERABAD','Hyderabad'), ('IMPHAL', 'Imphal'), ('INDORE', 'Indore'), ('JBALPUR', 'Jabalpur'), ('JAIPUR', 'Jaipur'), ('JAISALMAR', 'Jaisalmer'),
        ('JALANDHAR','Jalandhar'), ('JAMSHEDPUR', 'Jamshedpur'), ('JODHPUR','Jodhpur'), ('JANAGARH', 'Junagadh'), ('KANPUR','Kanpur'), ('KANYAKUMARI','Kanyakumari'), ('KHAJURAHO', 'Khajuraho'), ('KHANDALA', 'Khandala'), ('KOCHI','Kochi'), ('KODAIKANAL','Kodaikanal'),
        ('KILKATA', 'kolkata'), ('KOTA','Kota'), ('KOTTAYAM', 'Kottayam'), ('KOVALAM', 'Kovalam'), ('LUCKNOW', 'Lucknow'), ('LUDHIANA', 'Ludhiana'), ('MADURAI', 'Madurai'), ('MANALI', 'Manali'), ('MANGALORE', 'Mangalore'),
        ('MARGAO', 'Margao'), ('MATHURA','Mathura'), ('MOUNRABU', 'Mountabu'), ('MUMBAI', 'Mumbai'), ('MUSSORIE','Mussoorie'),('MYSORE',  ' Mysore'), ('MANALI', 'Manali'), ('NAGPUR', 'Nagpur'), ('NAINITAL', 'Nainital'), ('NOIDA','Noida'), ('OOTY', 'Ooty'),
        ('ORCHHA', 'Orchha'), ('PANAJI', 'Panaji'), ('PATNA', 'Patna'), ('PONDICHERRY','Pondicherry'), ('PORBANDAR','Porbandar'), ('PORTBLAIR', 'Portblair'), ('PUNE', 'Pune'), ('PURI', 'Puri'), ('PUSHKAR', 'Pushkar'), ('RAJKOT', 'Rajkot'), ('RAMESHWARAM', 'Rameswaram'), ('RANCHI', 'Ranchi'), ('SANCHI', 'Sanchi'), ('SECUNDERABAD', 'Secunderabad'),
        ('SHIMLA', 'Shimla'), ('SURAT', 'Surat'), ('THAJAVUR','Thanjavur'), ('THIRUCHIRAPALLI','Thiruchchirapalli'), ('THRISSUR', 'Thrissur'), ('TIRUMALA', 'Tirumala'), ('UDAIPUR', 'Udaipur'), ('VADODRA', 'Vadodra'), ('VARANASI', 'Varanasi'),
        ('VASCO-DA-GAMA', 'Vasco - Da - Gama'), ('VIJAYAWADA', 'Vijayawada'), ('VISAKHAPATNAM','Visakhapatnam')
    ]
    city = models.CharField(max_length=100, choices=service_level_choice)
    address = models.CharField(max_length=250, default="")
    otp = models.CharField(max_length=200, null=True)
    otp_gen_time = models.DateTimeField()
    token = models.CharField(max_length=200, default="")
    account_creation = CustomDateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()
    def __str__(self):
        st = "%s - %s(%s)" % (self.user_id, self.email, self.city)
        return st
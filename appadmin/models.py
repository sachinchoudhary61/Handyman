from django.db import models
from buisnessuser.models import Professional_user
# Create your models here.
class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Business_category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    people_involve = models.IntegerField(default=0)
    account_creation = CustomDateTimeField(auto_now_add=True)
    def __str__(self):
        st = "%s  -   %s" % (self.id, self.name)
        return st
class Business_Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    service_level_choice = [
        ('SIMPLE', 'Simple'),
        ('PREMIUM', 'Premium\n(Extra Care)')
    ]
    service_level = models.CharField(max_length=100, choices=service_level_choice, default='SIMPLE')
    Business_category = models.ForeignKey(Business_category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    people_involve_in_service = models.IntegerField(default=0)
    service_creation = CustomDateTimeField(auto_now_add=True)

    def __str__(self):
        st = "%s - %s(%s)" % (self.id, self.name, self.Business_category)
        return st

class Business_Service_info(models.Model):
    info_id = models.AutoField(primary_key=True)
    ServiceProvider_id = models.ForeignKey(Professional_user, on_delete=models.CASCADE)
    service_info = models.ForeignKey(Business_Service, on_delete=models.CASCADE)
    service_price = models.IntegerField(default=0)
    Profession_Experience = models.IntegerField(default=0)
    def __str__(self):
        st = "%s - %s(%s)" % (self.info_id, self.ServiceProvider_id, self.service_info)
        return st

from django.db import models


class NormalUser(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=False, null=True)
    is_delete = models.BooleanField(default=False, null=True)
    is_block = models.BooleanField(default=False, null=True)
    email = models.CharField(unique=True, default="", max_length=200, blank=True)

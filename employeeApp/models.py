from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee_info(models.Model):
    name=models.CharField(max_length=100,unique=True)
    address=models.TextField()
    phone_number=PhoneNumberField(max_length=14)
    salary=models.IntegerField()
    designation=models.CharField(max_length=50)
    short_description=models.TextField()

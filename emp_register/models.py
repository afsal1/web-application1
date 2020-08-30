from django.forms import ModelForm,Textarea
from django.db import models

# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=100, default='first name')
    l_name = models.CharField(max_length=100, default='last name')
    username = models.CharField(max_length=100, default='user name')
    email = models.EmailField(max_length=100, default='email id')
    password1 = models.CharField(max_length=32, default='password') 
    

class Meta:
    db_table = "sda"



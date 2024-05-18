from django.db import models
from django.contrib.auth.models import User

class loging_info(models.Model):
   user = models.ForeignKey(User, on_delete= models.SET_NULL , null= True ,blank= True)
   
class user_details(models.Model):
    name = models.TextField(max_length=200)
    ids = models.TextField(max_length=200)
    password = models.TextField(max_length=200)
   

# Create your models here.

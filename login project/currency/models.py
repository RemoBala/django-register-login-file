
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class User_datas(models.Model):
    username = models.CharField(max_length=50,default="")
    mail = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=50,default="")
    confirmpassword = models.CharField(max_length=50,default="")

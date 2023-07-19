from django.db import models

# Create your models here.

class Tbl_Admin(models.Model):
	username=models.CharField(max_length=50,default='')
	email=models.CharField(max_length=50,default='')
	pswd=models.CharField(max_length=50,default='')

class Tbl_Company(models.Model):
	name=models.CharField(max_length=50,default='')
	email=models.CharField(max_length=50,default='')
	pswd=models.CharField(max_length=50,default='')
	website=models.CharField(max_length=100,default='')

class Tbl_Employee(models.Model):
	fname=models.CharField(max_length=50,default='')
	lname=models.CharField(max_length=50,default='')
	phone=models.CharField(max_length=50,default='')
	email=models.CharField(max_length=50,default='')
	pswd=models.CharField(max_length=50,default='')
	company=models.ForeignKey(Tbl_Company, on_delete=models.CASCADE, blank=True, null=True)
	
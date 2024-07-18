from django.db import models

# Create your models here.
class MainCategory(models.Model):
    maincategoryname=models.CharField(max_length=70,blank=False,default='')
    icon=models.ImageField(upload_to='static/')



class MySubCategory(models.Model):
    maincategoryid=models.ForeignKey(MainCategory,on_delete=models.CASCADE,default=1)
    subcategoryname=models.CharField(max_length=70,blank=False,default='')
    icon=models.ImageField(upload_to='static/')




class Brands(models.Model):
    brandname=models.CharField(max_length=70,blank=False,default='')
    icon=models.ImageField(upload_to='static/')


class Product(models.Model):
    maincategoryid=models.ForeignKey(MainCategory,on_delete=models.CASCADE,default=1)
    subcategoryid=models.ForeignKey(MySubCategory,on_delete=models.CASCADE,default=1)
    brandid=models.ForeignKey(Brands,on_delete=models.CASCADE,default=1)
    productname=models.CharField(max_length=70,blank=False,default='')
    description=models.CharField(max_length=150,blank=False,default='')
    icon=models.ImageField(upload_to='static/')


class ProductDetails(models.Model):
    maincategoryid=models.ForeignKey(MainCategory,on_delete=models.CASCADE,default=1)
    subcategoryid=models.ForeignKey(MySubCategory,on_delete=models.CASCADE,default=1)
    brandid=models.ForeignKey(Brands,on_delete=models.CASCADE,default=1)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    productsubname=models.CharField(max_length=70,blank=False,default='')
    description=models.CharField(max_length=150,blank=False,default='')
    qty=models.IntegerField(blank=False,default='')
    price=models.IntegerField(blank=False,default='')
    color=models.CharField(max_length=70,blank=False,default='')
    size=models.CharField(max_length=70,blank=False,default='')
    offerprice=models.IntegerField(blank=False,default='') 
    offertype=models.CharField(max_length=70,blank=False,default='')
    icon=models.TextField(default='')


class AdminLogin(models.Model):
    emailid=models.CharField(max_length=70,blank=False,default='',unique=True)
    mobileno=models.CharField(max_length=70,blank=False,default='',unique=True)
    adminname=models.CharField(max_length=70,blank=False,default='')
    password=models.CharField(max_length=70,blank=False,default='')
    picture=models.CharField(max_length=70,blank=False,default='')


class Banner(models.Model):
    bannerdescription=models.CharField(max_length=70,blank=False,default='')
    icon=models.TextField(default='')

class SignUp(models.Model):
    mobileno=models.CharField(max_length=15,blank=False,primary_key=True,default='')
    fname=models.CharField(max_length=70,blank=False,default='')
    lname=models.CharField(max_length=70,blank=False,default='')
    emailid=models.CharField(max_length=70,blank=False,default='',unique=True)
    password=models.CharField(max_length=70,blank=False,default='')

class UserAddress(models.Model):
    mobileno=models.ForeignKey(SignUp,on_delete=models.CASCADE)
    country=models.CharField(max_length=70,blank=False,default='')
    address=models.CharField(max_length=70,blank=False,default='')
    city=models.CharField(max_length=70,blank=False,default='')
    postcode=models.CharField(max_length=70,blank=False,default='')

# class Search(models.Model):
    
#     name=models.CharField(max_length=70,blank=False,default='')
    

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator
class UserProfile(models.Model):
	 user = models.OneToOneField(User,  on_delete=models.CASCADE)
	 date = models.DateTimeField(default=timezone.now, blank=True)
	 phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
	 phone_number = models.CharField(max_length=10,validators=[phone_regex], blank=True)
	 ad_type= (
        ('1', 'RealEstate'),
        ('2', 'clothing'),
        ('3', 'Jewellery'),
        ('4', 'Movies'),
        ('5', 'TV'),
        ('6', 'radio'),
        ('7', 'footwear'),
        ('8', 'malls'),
        ('9', 'airport'),
        ('10', 'food'),
        ('11', 'fashion'),
        ('12', 'electronics'),
        ('13', 'pharmacy'),
        ('14', 'hospital'),
        ('15', 'print_media'),
        ('16', 'Banks'),
        ('17', 'Theme parks'),
        ('18', 'Tourism'),
        ('19', 'Travel'),
        ('21', 'E-Commerce'),
        ('22', 'Telephone'),
        ('23', 'Mobiles'),
        ('24', 'Grocers'),
        ('25', 'Computers & Accesories'),
        ('26', 'Sports-Outdoors'),
        ('27', 'Furniture'),
        ('28', 'others')
        )
         ad_type = models.CharField(max_length=120,choices=ad_type,default=1,)
         address = models.TextField(max_length=500,blank=False,default="Address")
         city = models.CharField(max_length=100,default="Hyderabad",)
         pincode = models.IntegerField(default=500032,)
	 first_name = models.CharField(max_length=100,blank=True)
	 #email_id =   models.EmailField(max_length=70,blank=True)
	 last_name =  models.CharField(max_length=100,blank=True)
	 def __unicode__(self):
		 return self.user.username
class UploadAdvetisement(models.Model):
        uploader = models.ForeignKey('auth.User')
        upload_Advertisement=models.FileField(upload_to='uploads/')
	time_of_advertisement=models.IntegerField(default=30)
	no_of_slots = models.IntegerField(default=1,)
	# select_bundles = (
	# (1, '1'),
    #     (2, '2'),
    #     (3, '3'),
    #     (4, '4'),
    #     (5, '5'),
    #     (6, '6'),
	# )
	no_of_repeats= models.IntegerField(default=1,)
	select_bundles = models.IntegerField(
        default=1,)
	no_of_weeks=(
	(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
	)
	no_of_weeks = models.IntegerField(choices=no_of_weeks,
        default=1,)
	date = models.DateTimeField(default=timezone.now, blank=True)
	bussinessPoint_longitude=models.DecimalField(max_digits=18,decimal_places=15,default=0)
	bussinessPoint_latitude=models.DecimalField(max_digits=18,decimal_places=15,default=0)
	start_week = models.DateTimeField('Starting week of the advertisement',default=timezone.now())
	amount_paid = models.IntegerField()
class Add_Device(models.Model):
        Username= models.CharField(max_length=40, default="Enter_Useranme",blank=False,unique=True)
        password =  models.CharField(max_length=62)

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
'''class UserProfile(models.Model):
	MERCHANT = 'ME'
	USER = 'US'
	user = models.OneToOneField(User)
	APPLYING_AS_A = (
        (MERCHANT, 'Merchant'),
        (USER, 'User'),
	)
	applying_as_a = models.CharField(
        max_length=2,
        choices=APPLYING_AS_A,
        default=USER,)
	def __unicode__(self):
        	return self.user.username
	def is_upperclass(self):
		return self.applying_as_a in (self.MERCHANT)'''

class UploadAdvetisement(models.Model):
        uploader = models.ForeignKey('auth.User')
        upload_Advertisement=models.FileField(upload_to='documents/')
	time_of_advertisement=models.IntegerField(default=30)
	no_of_slots= (
        (1, '1'),
        (2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	(6, '6'),
        )
	no_of_slots = models.IntegerField(choices=no_of_slots,
        default=1,)
	select_bundles = (
	(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
	)
	select_bundles = models.IntegerField(choices=select_bundles,
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
	bussinessPoint_longitude=models.DecimalField(max_digits=12,decimal_places=9,default=0)
	bussinessPoint_latitude=models.DecimalField(max_digits=12,decimal_places=9,default=0)
class Add_Device(models.Model):
        Username= models.CharField(max_length=16, default="Enter_Useranme",blank=False,unique=True)
        #password = models.CharField(max_length=32, widget=models.PasswordInput)
        password =  models.CharField(max_length=32)                                                                                      

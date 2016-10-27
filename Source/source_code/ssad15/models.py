from __future__ import unicode_literals

from django.db import models


class advertisement(models.Model):
    upload = models.FileField(upload_to='uploads/')
    time_len = models.IntegerField(default=30)

class zone(models.Model):
    bottom_left_coordinate_x=models.DecimalField(max_digits=20,decimal_places=17,default=0)
    bottom_left_coordinate_y=models.DecimalField(max_digits=20,decimal_places=17,default=0)
class zone_cost(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    cost = models.IntegerField(default=-1)
class slots(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    slot_no = models.IntegerField(default=0)
    no_of_bundles_used = models.IntegerField(default=0)
class scheduler(models.Model) :
    slots_id = models.ForeignKey(slots, on_delete=models.CASCADE)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    is_starting = models.BooleanField(default=True)

class slot(models.Model):
    zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    is_starting = models.BooleanField(default=True)
    bundles_used = models.DecimalField(max_digits=5,decimal_places=2,default=0)

class running(models.Model) :
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    alloted = models.IntegerField(default=0)


class devices(models.Model):
    username=models.CharField(max_length=10,unique=True)

# class zone(models.Model):
#     total_bundles=models.IntegerField(default=10)
#     bundles_used=models.IntegerField(default=0)
#     cost=models.DecimalField(default=100,max_digits=10,decimal_places=2)
#     bottom_left_coordinate_x=models.DecimalField(max_digits=18,decimal_places=15,default=0)
#     bottom_left_coordinate_y=models.DecimalField(max_digits=18,decimal_places=15,default=0)
#
# class advertisement(models.Model):
#     upload = models.FileField(upload_to='uploads/')
#
# class slot(models.Model):
#     zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
#     slot_no = models.IntegerField(default=0)
#     advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
#     bundles_used = models.DecimalField(max_digits=5,decimal_places=2,default=0)
#
#
#
# #to store  device ids of configured devices
# #to be decided if username of device will be alphanumeric or numeric string
# class devices(models.Model):
#     username=models.CharField(max_length=10,unique=True)
# class running(models.Model):
#     slot_no = models.IntegerField(default=0)
#     zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)

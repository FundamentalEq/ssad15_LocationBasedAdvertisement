from __future__ import unicode_literals

from django.db import models



class zone(models.Model):
    total_bundles=models.IntegerField(default=10)
    bundles_used=models.IntegerField(default=0)
    cost=models.DecimalField(default=100,max_digits=10,decimal_places=2)
    bottom_left_coordinate_x=models.DecimalField(max_digits=12,decimal_places=9,default=0)
    bottom_left_coordinate_y=models.DecimalField(max_digits=12,decimal_places=9,default=0)

class advertisement(models.Model):
    upload = models.FileField(upload_to='uploads/')

class slot(models.Model):
    zone_id = models.ForeignKey(zone, on_delete=models.CASCADE)
    slot_no = models.IntegerField(default=0)
    advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    bundles_used = models.DecimalField(max_digits=5,decimal_places=2,default=0)



#to store  device ids of configured devices
#to be decided if username of device will be alphanumeric or numeric string
class devices(models.Model):
    username=models.CharField(max_length=10,unique=True)

# import os
# import time
# from django_cron import cronScheduler, Job
from django_cron import CronJobBase, Schedule
from userauth.models import *
from ssad15.models import *
from django.utils import timezone
from global_values import *

def getzone(longitude,latitude):
    x = longitude
    y = latitude
    rows_done = math.floor((y- bottom_extreme)/dely)
    in_a_row = math.floor((x - left_extreme)/delx)
    zone_no = rows_done*zonesAlongX + in_a_row
    return int(zone_no)


print "the transfer script is running at "  , timezone.now()
def do_transfer() :
    for userinput in UploadAdvetisement.objects.all() :
        xcenter = float(userinput.bussinessPoint_longitude)
        ycenter = float(userinput.bussinessPoint_latitude)
        left = xcenter - DELX/2
        right = xcenter + DELX/2
        bottom = ycenter - DELY/2
        top = ycenter + DELY/2
        y = ycenter - (DELY/2)
        ad = advertisement(upload=userinput.upload_Advertisement)
        ad.save()
        print "ad is = ",ad.id
        while y < (ycenter + DELY/2) :
            x = xcenter - (DELX/2)
            while x < (xcenter + DELX/2) :
                zone_no = getzone(x,y)
                print "zone no is",zone_no
                my_zone = zone.objects.filter(id = int(zone_no))
                print "my zone" , my_zone[0].id
                #**********to be done**********
                #calculating the area
                # xx = my_zone[0].bottom_left_coordinate_x
                # yy = my_zone[0].bottom_left_coordinate_y
                # if xx >= bottom :

                #******kam chalo for r1****
                prev = slot.objects.filter(zone_id=my_zone[0].id)
                my_slot_no = len(prev)+1
                sl = slot(zone_id_id=int(my_zone[0].id),advertisement_id_id=ad.id,slot_no=my_slot_no)
                sl.save()
                print "sl id is",sl.id

                x = x + delx
            y = y + dely

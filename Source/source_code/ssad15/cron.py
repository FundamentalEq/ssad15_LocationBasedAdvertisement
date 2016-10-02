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

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ssad15.my_cron_job'    # a unique code

    def do(self):
        print "the transfer script is running at "  , timezone.now()
        temp = UploadAdvetisement.objects.all()
        print temp 
        for userinput in temp :
            xcenter = userinput.bussinessPoint_longitude
            ycenter = userinput.bussinessPoint_latitude
            print xcenter,ycenter
            pass
            y = ycenter - (DELY/2)
            while y < ycenter + DELY :
                x = xcenter - (DELX/2)
                while x < xcenter + DELX :
                    zone_no = getzone(x,y)
                    print int(zone_no)
                # my_zone = zone.objects.filter(id=)

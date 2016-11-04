from ssad15.models import zone,zone_info,running_slots #the databse where the entries will be stored
from global_values import *
import datetime
# assming that for both longitutde and latitude  1 degree = 111 Km
# thought the distance between 2 longitutde and latitude is not constant
# but since The India lies near equator and our size of each zone = 1Km
# our assumption will introduce a marginal error that can be ignored

# print delx,dely
x,y = left_extreme,bottom_extreme
zone_no = 1
cur  = datetime.datetime.now()
while y < top_extreme :
    x = left_extreme
    while x < right_extreme :
        print x,y,zone_no
        z = zone(bottom_left_coordinate_x=x,bottom_left_coordinate_y=y)
        z.save()
        zone_info(zone_id=z.id,week=0,cost=100,no_of_bundles=10).save()
        running_slots(zone_id=z.id,slot=1,start_time=cur).save()
        zone_no += 1
        x += delx
    y += dely

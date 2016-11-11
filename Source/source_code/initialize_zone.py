from ssad15.models import zone,zone_info,running_slots #the databse where the entries will be stored
from global_values import *
import datetime
# assming that for both longitutde and latitude  1 degree = 111 Km
# thought the distance between 2 longitutde and latitude is not constant
# but since The India lies near equator and our size of each zone = 1Km
# our assumption will introduce a marginal error that can be ignored

# the code written below intialize the database for the first time before the prodct can be used
# it is meant to populate zone table , whos values wont change throught the usage of the product
# zone_info that stores the initial value for the cost of advertisement for each zone and no of bundles in each zone
x,y = left_extreme,bottom_extreme
zone_no = 1
# store the time of population of the database meant to be as min time
cur  = datetime.datetime.now()
while y < top_extreme :
    x = left_extreme
    while x < right_extreme :
        print x,y,zone_no
        # making entery into zone table
        z = zone(bottom_left_coordinate_x=x,bottom_left_coordinate_y=y)
        z.save()
        #making entery into zone_info table
        zone_info(zone_id=z.id,week=0,cost=100,no_of_bundles=10).save()
        running_slots(zone_id=z.id,slot=1,start_time=cur).save()
        zone_no += 1
        x += delx
    y += dely

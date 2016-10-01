from django.shortcuts import render
from django.http import HttpResponse
from global_values import *

def index(request):
    return HttpResponse("Hello")


# Get zone correponding to the location pinged by the device
def getzone(longitude,latitude):
    x = longitude
    y = latitude
    rows_done = math.floor((y- bottom_extreme)/dely)
    in_a_row = math.floor((x - left_extreme)/delx)
    zone_no = rows_done*zonesAlongX + in_a_row
    return int(zone_no)
# get advertisment corresponding to the zone device is in and also the server time
def get_advertisement(zone_id):


#get the pinged location from the device
def pinged_location(request):
    if request.method == 'POST':
        if 'longitude' in request.POST:
            longitude = request.POST['longitude']
        else :
            error=1
        if 'latitude' in request.POST :
            latitude=request.POST['latitude']
        else :
            error=1

    if error == 1:
        return HttpResponse("Error in getting location !")
    else :
        zone_no=getzone(longitude,latitude)
        get_advertisement(zone_no)

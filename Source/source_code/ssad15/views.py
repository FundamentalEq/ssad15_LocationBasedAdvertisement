from django.shortcuts import render
from django.http import HttpResponse
from global_values import *
from django.template import loader
from .models import zone,slot,advertisement
from django.shortcuts import get_list_or_404,get_object_or_404
import datetime

def index(request):
    return HttpResponse("Location Based Advertising")


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
    current_time=datetime.datetime.now()
    #calculating slot number from 1 to 120
    slot_no=int((current_time.minute * 60 + current_time.second)/30)
    slot=get_object_or_404(slot,zone_id=zone_id_id,slot_no=slot_no)
    ad_id=slot.advertisement_id_id
    ad=get_object_or_404(advertisement,pk=ad_id)
    path=ad.upload
    path=str(path)
    return path

#get the pinged location from the device
#get corresponding zone no and display advertisement according to time and zone
#this function to be changed for scheduling in R2
def display_advertisement(request):
    #checking if location is posted or not
    #error set to 1 represents an error in getting location of the device
    if request.method == 'GET':
        if 'longitude' in request.GET:
            longitude = request.GET['longitude']
        else :
            error=1
        if 'latitude' in request.GET :
            latitude=request.GET['latitude']
        else :
            error=1

    if error == 1:
        return HttpResponse("Error in getting location !")
    else :
        zone_no=getzone(longitude,latitude)
        path=get_advertisement(zone_no)
        context={'path':path}
        return render(request, 'ssad15/display_advertisement.html', context)
#after device is logged in,it will be redirected to this controller
def start_advertisement(request):
    return render(request,'ssad15/start_advertisement.html')

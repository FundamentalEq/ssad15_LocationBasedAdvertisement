from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello")


# Get zone correponding to the location pinged by the device
def getzone(longitude,latitude):


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

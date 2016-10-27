from django.shortcuts import render
from django.http import HttpResponse
from global_values import *
from django.template import loader
from .models import *
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

def getOverLappingArea(left,right,bottom,top,zone_no):
    Zone = zone.objects.filter(id=zone_no)[0]
    lowerx = Zone.bottom_left_coordinate_x
    lowery = Zone.bottom_left_coordinate_y
    topx = lowerx + delx
    topy = lowery + dely
    l = max(lowerx,left)
    r = min(topx,right)
    b = max(lowery,bottom)
    t = min(topy,top)
    return float((r-l)*(t-b))

def getWeekNumber(cur_date) :
    return datetime.date(cur_date.year,cur_date.month,cur_date.day).isocalendar()[1]

def check_for_slot(zone_no,required_bundles,required_slots,cont_slots,sets,week_no,total_bundles) :
    Slots = slots.objects.filter(zone_id = zone_no,week = week_no)
    total_bundles = 10
    info = zone_info.objects.filter(zone_id = zone_no ,week = week_no)
    if info :
        total_bundles = info.no_of_bundles
    for slot in Slots :
        if total_bundles -slot.no_of_bundles_used >= required_bundles :
            sets -= 1
            if sets == 0 :
                return True
    if len(Slots) + sets <= MAX_SLOTS :
        return True
    return False

def check_availability(request) :
    print "***************************the check function has been called"
    Xcenter = float(request.bussinessPoint_longitude)
    Ycenter = float(request.bussinessPoint_latitude)
    left = Xcenter - DELX/2
    right = Xcenter + DELX/2
    bottom = Ycenter - DELY/2
    top = Ycenter + DELY/2
    # starting the loop to map the request into zones and check the availability
    y = bottom
    week_no = getWeekNumber(request.start_week)
    cont_slots = math.ceil(request.time_of_advertisement/30.0)
    sets = request.no_of_slots / cont_slots

    while y < top :
        x = left
        while x < right :
            zone_no = getzone(x,y)
            OArea = getOverLappingArea(left,right,bottom,top,zone_no)
            required_bundles = (OArea/BAREA)*request.select_bundles ;
            if not check_for_slot(zone_no,required_bundles,request.no_of_slots,cont_slots,sets,week_no,total_bundles) :
                return False ;
            x += delx
        y += dely
    return True
# get advertisment corresponding to the zone device is in and also the server time
def get_advertisement(Zone_id):
    # current_time=datetime.datetime.now()
    #calculating slot number from 1 to 120
    # slot_no=int((current_time.minute * 60 + current_time.second)/30)
    Slot=running.objects.filter(zone_id=Zone_id)[0]
    tot = slot.objects.filter(zone_id=Zone_id)
    tot_slots = len(tot)
    if tot_slots == 0 :
        pass # to handeled later
    Slot.slot_no = Slot.slot_no + 1
    if Slot.slot_no > tot_slots :
        Slot.slot_no=1
    slot_no=Slot.slot_no
    print "the current slot is ",slot_no
    Slot.save()
    SSlot=get_object_or_404(slot,zone_id_id=Zone_id,slot_no=slot_no)
    ad_id=SSlot.advertisement_id_id
    ad=get_object_or_404(advertisement,pk=ad_id)
    print "Ad is ",ad
    path=ad.upload.url
    path=str(path)
    return path

#get the pinged location from the device
#get corresponding zone no and display advertisement according to time and zone
#this function to be changed for scheduling in R2
import json
def display_advertisement(request):
    #checking if location is posted or not
    #error set to 1 represents an error in getting location of the device
    error = 0
    if request.method == 'POST':
        if 'longitude' in request.POST:
            longitude = float(request.POST['longitude'])
        else :
            error=1
        if 'latitude' in request.POST :
            latitude= float(request.POST['latitude'])
        else :
            error=1
    else :
        error = 1
    print float(longitude),float(latitude)
    if error:
        return HttpResponse("Error in getting location !")
    else :
        zone_no=getzone(longitude,latitude)
        print "zone no is ",zone_no
        path=get_advertisement(zone_no)
        # path = "media/" + path
        print "path fron db is",path
        # path = "chaitanya"
        context={'path':path}
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )
        # return render(request, 'ssad15/display_advertisement.html', context)
#after device is logged in,it will be redirected to this controller
def start_advertisement(request):
    return render(request,'ssad15/start_advertisement.html')
def render_advertisement(request):
    return render(request,'ssad15/render_advertisement.html')

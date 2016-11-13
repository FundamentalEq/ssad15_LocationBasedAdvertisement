from django.shortcuts import render
from django.http import HttpResponse
from global_values import *
from django.template import loader
from .models import *
from django.shortcuts import get_list_or_404,get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from forms import *
from decimal import *
import json

def index(request):
    return HttpResponse("Location Based Advertising")


# Get zone correponding to the location pinged by the device
def getzone(longitude,latitude):
    print longitude,latitude
    x = longitude
    y = latitude
    rows_done = math.floor((y- bottom_extreme)/dely)
    in_a_row = math.floor((x - left_extreme)/delx)
    zone_no = rows_done*zonesAlongX + in_a_row + 1
    zone_no = int(zone_no)
    # test code
    Zone = zone.objects.filter(id=zone_no)
    # error handling
    if len(Zone) == 0 :
        # => that an invalid location has been picked
        # raise error
        print "Invalid location has been entered by the user"
        return 0
    else :
        # select the required zone
        Zone = Zone[0]

    lowerx = Zone.bottom_left_coordinate_x
    lowery = Zone.bottom_left_coordinate_y
    topx = Decimal(lowerx) + Decimal(delx)
    topy = Decimal(lowery) + Decimal(dely)
    if lowery <= latitude and latitude <=topy  and lowerx <= longitude and longitude <= topx :
        print "Valid zone number"
    else :
        print "the zone number so caluclated does not match the records"
        print "lowerx = ",lowerx
        print "topx = " ,topx
        print "lowery = ",lowery
        print "topy = ",topy
    return zone_no

def getOverLappingArea(left,right,bottom,top,zone_no):
    print "required zone no is ",zone_no
    Zone = zone.objects.filter(id=zone_no)
    # error handling
    if len(Zone) == 0 :
        # => that an invalid location has been picked
        # raise error
        print "Invalid location has been entered by the user"
        return False
    else :
        # select the required zone
        Zone = Zone[0]

    lowerx = Zone.bottom_left_coordinate_x
    lowery = Zone.bottom_left_coordinate_y
    topx = Decimal(lowerx) + Decimal(delx)
    topy = Decimal(lowery) + Decimal(dely)
    l = Decimal(max(lowerx,left))
    r = Decimal(min(topx,right))
    b = Decimal(max(lowery,bottom))
    t = Decimal(min(topy,top))
    area = Decimal((r-l)*(t-b))
    #converting degree to Km
    area = area * kmTodegree * kmTodegree

    if area < 0.0 :
        # this zone does not overlap with the required bussiness area
        # area = 0
        print "Warning : area is -ve"
        area = Decimal(0)

    return area

def getWeekNumber(cur_date) :
    return datetime.date(cur_date.year,cur_date.month,cur_date.day).isocalendar()[1]

def check_for_slot(zone_no,required_bundles,required_slots,cont_slots,sets,week_no) :
    Slots = slots.objects.filter(zone_id = zone_no,week = week_no).order_by('slot_no')
    total_bundles = DEFAULT_BUNDLES

    # pre condition : zone_info should have been populated atleast once : initilize_zone.py
    info = zone_info.objects.filter(zone_id = zone_no).order_by('-week')
    if len(info)!=0 :

        # find if the total no of bundles have been modified by the Admin
        # if yes find the most recent modification and use that
        for inf in info :
            if inf.week <= week_no :
                total_bundles = inf.no_of_bundles
                break

    else :

        #error raised
        # probable cause database has not been populated
        #displaying appropriate warnings
        print "Warning : Admin : Database has not been populated"
        print "Run initilize_zone.py to rectify the error"
        redirect(invalid_empty_database)

    # algorithm to check avaialable availability of slots

    i=0
    while i < len(Slots) :
        slot = Slots[i]
        valid = True
        for j in range(cont_slots) :
            if i+j+1 > len(Slots) and i+j+1 <= MAX_SLOTS :
                pass
            elif i+j+1 <= len(Slots) and total_bundles - Slots[i+j].no_of_bundles_used >= required_bundles :
                pass
            else :
                valid = False
                break
        if valid :
            sets -= 1
            i += cont_slots
            if sets == 0 :
                # if the demand has been met return true
                return True
        else :
            i += 1
    if len(Slots) + sets*cont_slots <= MAX_SLOTS :
        # if the demand can be met
        return True

    # slots are not avaialable in the given zone
    return False

def check_availability(request) :

    # intializing the variables need for the calculations
    Xcenter = Decimal(request.bussinessPoint_longitude)
    Ycenter = Decimal(request.bussinessPoint_latitude)
    left = Xcenter - DELX/2
    right = Xcenter + DELX/2
    bottom = Ycenter - DELY/2
    top = Ycenter + DELY/2

    # starting the loop to map the request into zones and check the availability
    y = bottom
    wn = getWeekNumber(request.start_week)
    wn = int(wn)

    # the number of slots that must be given in continuous
    # eg a 45 second add must be given 2 slots at min in continuous to be displayed
    cont_slots = math.ceil(request.time_of_advertisement/30.0)
    cont_slots = int(cont_slots)

    # sets is the times an advertisement have to be displayed
    sets = request.no_of_slots / cont_slots
    sets = int(sets)

    while y < top :
        x = left
        while x < right :

            # find the zone no based the coordinates
            zone_no = getzone(x,y)

            # get the overlap area between the bussiness area wrt to the current point and the zone
            OArea = getOverLappingArea(left,right,bottom,top,zone_no)
            if OArea == False :
                # error has been raised
                # the user has inputed an invalid location
                redirect(invalid_location)

            # the number of bundles that needs to be given to the current advertisement in the current zone
            required_bundles = (OArea/BAREA)*request.select_bundles

            # calls the check_for_slot() to check for availability of slots in the current zone for all the required weeks
            for week_no in range(int(request.no_of_weeks)) :
                week_no += wn
                if not check_for_slot(zone_no,required_bundles,request.no_of_slots,cont_slots,sets,week_no) :
                    # no slots are avaialable in the current zone
                    # rasie error
                    return False

            x += delx
        y += dely

    return True


def update_slot(zone_no,required_bundles,cont_slots,sets,week_no,ad,bundles_info):
    # changing data type to avoid precision errors
    required_bundles = Decimal(required_bundles)
    # algorithm for Updating the database
    print "required_bundles = ",required_bundles
    Slots = slots.objects.filter(zone_id= zone_no,week=week_no).order_by('slot_no')

    total_bundles = DEFAULT_BUNDLES
    if len(bundles_info)!=0 :

        # find if the total no of bundles have been modified by the Admin
        # if yes find the most recent modification and use that
        for inf in bundles_info :
            if inf.week <= week_no :
                total_bundles = inf.no_of_bundles
                break

    else :

        #error raised
        # probable cause database has not been populated
        #displaying appropriate warnings
        print "Warning : Admin : Database has not been populated"
        print "Run initilize_zone.py to rectify the error"
        redirect(invalid_empty_database)

    i=0
    while i < len(Slots) :

        valid = True
        for j in range(cont_slots) :
            if i+j+1 > len(Slots) and i+j+1 <= MAX_SLOTS :
                pass
            elif i+j+1 <= len(Slots) and total_bundles - Slots[i+j].no_of_bundles_used >= required_bundles :
                pass
            else :
                valid = False
                break

        if valid :
            # found the slot ,where the entery can be made
            for j in range(cont_slots) :
                # if the i+j+1 slot already exist
                if i+j+1 <= len(Slots) :
                    slot = Slots[i+j]
                    slot.no_of_bundles_used += required_bundles
                    slot.save()
                    start = False
                    if j == 0 :
                        start = True
                    schedule = scheduler(slots_id_id=slot.id,advertisement_id_id=ad.id,
                                         bundles_tobegiven=required_bundles,
                                         is_starting=start)
                    schedule.save()
                # the entery corresponding to the given slot number does not already exist in the database
                # thus first we need to make an entery into the slot table and then
                # update the scheduler table
                else :
                    slot = slots(zone_id=zone_no,week=week_no,slot_no=int(i+j+1),
                                 no_of_bundles_used=0)
                    slot.no_of_bundles_used += required_bundles
                    slot.save()
                    start = False
                    if j == 0 :
                        start = True
                    schedule = scheduler(slots_id_id=slot.id,advertisement_id_id=ad.id,
                                         bundles_tobegiven=required_bundles,
                                         is_starting=start)
                    schedule.save()

            i += cont_slots
            sets -= 1
            if sets == 0 :
                break
        else :
            i += 1

    if sets > 0 :
        # to adjsut indexing
        i += 1
        while sets > 0 :
            for j in range(cont_slots) :
                slot = slots(zone_id=zone_no,week=week_no,slot_no=int(i+j),
                             no_of_bundles_used=0)
                slot.no_of_bundles_used += required_bundles
                slot.save()
                start = False
                if j == 0 :
                    start = True
                schedule = scheduler(slots_id_id=slot.id,advertisement_id_id=ad.id,
                                     bundles_tobegiven=required_bundles,
                                     is_starting=start)
                schedule.save()
            sets -= 1
            i += cont_slots
    #the update complete

def update_scheduler(request) :
    # making sure that the slot is still avaialable
    if not check_availability(request) :
        # slots are no longer available
        return False

    else :
        # availability still holds good
        # intializing the variables need for the calculations
        Xcenter = Decimal(request.bussinessPoint_longitude)
        Ycenter = Decimal(request.bussinessPoint_latitude)
        left = Xcenter - DELX/2
        right = Xcenter + DELX/2
        bottom = Ycenter - DELY/2
        top = Ycenter + DELY/2

        # starting the loop to map the request into zones and check the availability
        y = bottom
        wn = getWeekNumber(request.start_week)
        wn = int(wn)

        # the number of slots that must be given in continuous
        # eg a 45 second add must be given 2 slots at min in continuous to be displayed
        cont_slots = math.ceil(request.time_of_advertisement/30.0)
        cont_slots = int(cont_slots)

        # sets is the times an advertisement have to be displayed
        sets = request.no_of_slots / cont_slots
        sets = int(sets)

        # add the advertisement to advertisement table
        ad = advertisement(upload=request.upload_Advertisement,time_len=request.time_of_advertisement)
        ad.save()

        # looping through the map
        while y < top :
            x = left
            while x < right :

                # find the zone no based the coordinates
                zone_no = getzone(x,y)

                # get the overlap area between the bussiness area wrt to the current point and the zone
                OArea = getOverLappingArea(left,right,bottom,top,zone_no)
                if OArea == False :
                    # error has been raised
                    # the user has inputed an invalid location
                    redirect(invalid_location)

                # the number of bundles that needs to be given to the current advertisement in the current zone
                required_bundles = (OArea/BAREA)*request.select_bundles

                # geting data about max available bundles in the current zone
                # pre condition : zone_info should have been populated atleast once : initilize_zone.py
                bundles_info = zone_info.objects.filter(zone_id = zone_no).order_by('-week')

                #update the slots for all the required weeks for the current zone
                for week_no in range(int(request.no_of_weeks)) :
                    week_no += wn
                    update_slot(zone_no,required_bundles,cont_slots,sets,week_no,ad,bundles_info)

                x += delx
            y += dely
        for week_no in range(int(request.no_of_weeks)) :
            week_no += wn

        return True


# get advertisment corresponding to the zone device is in and also the server time

def find_slot_no(Zone_id) :
    # taking the current server time
    cur = datetime.datetime.now()

    cur_slot = running_slots.objects.all.filter(zone_id=Zone_id)
    if len(cur_slot) == 0 :

        # error raised
        # probable cause database has not been populated
        #displaying appropriate warnings
        print "Warning : Admin : Database has not been populated"
        print "Run initilize_zone.py to rectify the error"
        redirect(invalid_empty_database)

    else :

        # algorithm for calculating the current slot based on total number of slots present
        # and the time elapsed since the start of the current slot
        diff = (cur.minute - cur_slot.start_time.minute)*60 + (cur.second - cur_slot.start_time.second)
        change = math.floor(diff/30.0)
        change = int(change)

        if change > 0 :
            running.objects.filter(zone_id=Zone_id).delete()
            running_ads.objects.filter(zone_id=Zone_id).delete()

            # formula cur_slot = (pre_cur_slot + change - 1)%total_no_of_slots + 1
            max_avail_slots = len(slot.objects.filter(zone_id=Zone_id))
            cur_slot.slot = (cur_slot.slot + change - 1)%max_avail_slots + 1

            # updating the database
            cur_slot.save()

        return cur_slot.slot

def get_advertisement(Zone_id):

    #finding the current slot no for the current zone based on the server time and
    #total number of active slots in that zone
    slot_no = find_slot_no(Zone_id)

    # get all the advertisement in the current zone , whos display start in the
    # current zone
    all_adv = slot.objects.filter(zone_id_id=Zone_id,slot_no=slot_no,is_starting = True)

    if len(all_adv) == 0 :
        # no advertisement to be displayed in the current zone that starts in the current slot
        # need to pass some default advertisement
        pass

# to find the number of devices that have already been in the current zone current slot
    X = running.objects.filter(zone=Zone_id,slot_no=slot_no)
    if len(X) == 0 :
        X = running(zone_id=Zone_id,slot_no=slot_no,alloted=0)
    else :
        X = X[0]
    X.alloted += 1
    X.save()

    X = X.alloted

    # algorithm to find advertisement that should be displayed
    Ad = 0
    priority = 0
    for ad in all_adv :

        # no of devices that are already showing the current advertisement
        given = running_ads.objects.filter(zone_id=Zone_id,ad=ad.advertisement_id,slot_no=slot_no)

        if len(given) == 0 :
            # => no device has been alloted to current device in this slot
            # make a new entry in the table
            given = running_ads(zone_id=Zone_id,slot_no=slot_no,ad=ad.advertisement_id,given=0)
            given.save()
        else :
            given = given[0]

        if ad.bundles_tobegiven*X - given.given > priority :
            priority = ad.bundles_tobegiven*X - given.given
            Ad = ad.advertisement_id

    # Ad will have id of the advertisement that should be displayed

    cont_slots = math.ceil(cur_ad.time_len /30.0)
    cont_slots = int(cont_slots)

    for sl in range(slot_no+1,slot_no+cont_slots) :
        rs = running_slots.objects.filter(zone_id=Zone_id,slot=sl)
        if len(rs) == 0 :
            rs = running_slots(zone_id=Zone_id,slot=sl,alloted=0)
        else :
            rs = rs[0]
        rs.alloted += 1
        rs.save()
        ra = running_ads(zone_id=Zone_id,ad=cur_ad.id,slot_no=sl)
        if len(ra) == 0 :
            ra = running_ads(zone_id=Zone_id,slot_no=sl,given=0)
        else :
            ra = ra[0]
        ra.given += 1
        ra.save()
    my_ad=get_object_or_404(advertisement,id=Ad)
    path = my_ad.upload.url
    return str(path),my_ad.time_len

#get the pinged location from the device
#get corresponding zone no and display advertisement according to time and zone


def display_advertisement(request):
    #checking if location is posted or not
    #error set to 1 represents an error in getting location of the device
    error = 0
    if request.method == 'POST':
        if 'longitude' in request.POST:
            longitude = Decimal(request.POST['longitude'])
        else :
            error=1
        if 'latitude' in request.POST :
            latitude= Decimal(request.POST['latitude'])
        else :
            error=1
    else :
        error = 1
    print Decimal(longitude),Decimal(latitude)
    if error:
        return HttpResponse("Error in getting location !")
    else :
        zone_no=getzone(longitude,latitude)

        # get the required details about the advertisement to be displayed
        path,time_len=get_advertisement(zone_no)

        context={'path':path,'time_len':time_len}
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )


# function to calculate total cost to be paid by the customer
def total_cost(request):
    print "total cost has been called"
    # intializing the variables need for the calculations
    Xcenter = Decimal(request.bussinessPoint_longitude)
    Ycenter = Decimal(request.bussinessPoint_latitude)
    left = Xcenter - DELX/2
    right = Xcenter + DELX/2
    bottom = Ycenter - DELY/2
    top = Ycenter + DELY/2

    # starting the loop to map the request into zones and check the availability
    y = bottom
    wn = getWeekNumber(request.start_week)
    wn = int(wn)

    #variable to store total_cost
    total_cost=0

    # starting the loop to map the request into zones and calculate total cost
    # no of slots requested by the user
    no_of_slots=request.no_of_slots
    no_of_slots = int(no_of_slots)

    while y < top :
        x = left
        while x < right :

            # find the zone no based the coordinates
            zone_no = getzone(x,y)

            # get the overlap area between the bussiness area wrt to the current point and the zone
            OArea = getOverLappingArea(left,right,bottom,top,zone_no)
            if OArea == False :
                # error has been raised
                # the user has inputed an invalid location
                redirect(invalid_location)

            # the number of bundles that needs to be given to the current advertisement in the current zone
            required_bundles = (OArea/BAREA)*request.select_bundles

            zone_information = zone_info.objects.filter(zone_id=zone_no).order_by('-week')
            for week_no in range(int(request.no_of_weeks)) :
                week_no += wn
                i = 0
                select_week = -1
                cost = 0

                while i< len(zone_information):
                    if zone_information[i].week <= week_no:
                        select_week = zone_information[i].week
                        cost = zone_information[i].cost
                        break
                    else :
                        i += 1

                if select_week == -1 :
                    # error raised
                    # no cost available for the the given zone
                    #displaying appropriate warnings
                    print "Warning : Admin : Database has not been populated"
                    print "Run initilize_zone.py to rectify the error"
                    redirect(invalid_empty_database)

                total_cost = total_cost + required_bundles * cost * no_of_slots
            x += delx
        y += dely

    # returning the total cost that the merchant will have to pay
    return int(total_cost)

# to allow the admin to change the specifications about a zones :
# 1) cost of advertisement
# 2) Maxmimum number of budnles in that zones
# All the changes will take place starting the week specified

def select_zone(request) :

    # check for the proper authentication
    # only admin has access to select_zone
    if not request.user.is_superuser :
        # unauthorised access
        # raise error
        print "unauthorised access attempted by ",request.user
        redirect(unauthorised_access)

    else :
        # the user is the superuser
        print "Admin accessing select_zone at ", datetime.datetime.now()

    # error variable turns one if the location is not recieved
    error = 0

    if request.method == 'POST':
        # get the longitude
        if 'longitude' in request.POST:
            longitude = Decimal(request.POST['longitude'])
        else :
            error=1

        # get the latitude
        if 'latitude' in request.POST :
            latitude= Decimal(request.POST['latitude'])
        else :
            error=1

        # if the location was not recieved :
        if error:
            # raise error
            return redirect(invalid_location)

        else :
            # the coordinate of the point around which the changes have to made
            # have been successfully selected
            return redirect(edit_zone,longitude=longitude,latitude=latitude)
    else :
        # else simply allow the admin to select the zone
        return render(request,'ssad15/select_zone.html')
    return render(request,'ssad15/select_zone.html')

def edit_zone(request,longitude,latitude) :

    # check for the proper authentication
    # only admin has access to select_zone
    if not request.user.is_superuser :
        # unauthorised access
        # raise error
        print "unauthorised access attempted by ",request.user
        redirect(unauthorised_access)

    else :
        # the user is the superuser
        print "Admin accessing edit_zone at ", datetime.datetime.now()

    if request.method == 'POST' :

        # form to collect the info form the admin about the new changed values
        form =zone_info_form(request.POST)

        if form.is_valid() :
            print "changes done by the admin are valid"
            form = form.cleaned_data

            # intializing the variables need for the calculations
            Xcenter = Decimal(request.bussinessPoint_longitude)
            Ycenter = Decimal(request.bussinessPoint_latitude)
            left = Xcenter - DELX/2
            right = Xcenter + DELX/2
            bottom = Ycenter - DELY/2
            top = Ycenter + DELY/2

            y = bottom
            wn = getWeekNumber(form['week'])

            while y < top :
                x = left
                while x < right :

                    # find the zone no based the coordinates
                    zone_no = getzone(x,y)

                    # check if this a valid zone_no
                    check_zone = zone.objects.all.filter(id=zone_no)

                    if len(check_zone) == 0 :
                        # raise error
                        # invalid_location
                        redirect(invalid_location)

                    else :
                        zone_info(zone_id=zone_no,week=wn,cost=form['cost'],no_of_bundles=form['no_of_bundles']).save()

                    x += delx
                y += dely

            return render(request,'ssad15/changesdone.html')
        else :
            print "errors in the form submitted by the user ",request.user," = ", form.errors
    else :
        form = zone_info_form()
    return render(request,'ssad15/edit_zone.html',{'form':form,'longitude':longitude,'latitude':latitude})

#after device is logged in,it will be redirected to this controller
def start_advertisement(request):
    return render(request,'ssad15/start_advertisement.html')
def render_advertisement(request):
    return render(request,'ssad15/render_advertisement.html')

def invalid_location(request) :
    pass

def invalid_empty_database(request) :
    pass

def unauthorised_access(request) :
    pass

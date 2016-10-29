from ssad15.models import *
import datetime

def getWeekNumber(cur_date) :
    return datetime.date(cur_date.year,cur_date.month,cur_date.day).isocalendar()[1]

def do_transfer() :
    cur_date = datetime.datetime.now()
    week_no = getWeekNumber(cur_date)
    # clear the previous running table
    slot.objects.all().delete()
    running.objects.all().delete()
    #all the stale data has been deleted
    for s in slots.objects.filter(week=week_no) :
        for schedule in scheduler.objects.filter(slot_id=s.id) :
            entery = slot(zone_id_id=s.zone,slot_no=s.slot_no,
                          advertisement_id=schedule.advertisement_id,
                          is_starting=schedule.is_starting,
                          bundles_tobegiven=schedule.bundles_tobegiven)
            entery.save()
        #remove the data from the sceduler as it has already been copied to the current state database
        scheduler.objects.filter(slot_id=s.id).delete()
    slots.objects.filter(week=week_no).delete()

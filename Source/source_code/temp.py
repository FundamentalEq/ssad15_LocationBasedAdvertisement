from ssad15.models import *

for z in zone.objects.all() :
    r = running(zone_id_id=z.id,slot_no=0)
    r.save()
    print "zone = ",z.id,"run = ",r.id

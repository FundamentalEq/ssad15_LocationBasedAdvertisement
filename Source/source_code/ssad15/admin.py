from django.contrib import admin
from ssad15.models import advertisement
from ssad15.models import zone
from ssad15.models import zone_info
from ssad15.models import slots
from ssad15.models import slot
from ssad15.models import devices
admin.site.register(advertisement)
admin.site.register(zone)
admin.site.register(zone_info)
admin.site.register(slots)
admin.site.register(slot)
admin.site.register(devices)

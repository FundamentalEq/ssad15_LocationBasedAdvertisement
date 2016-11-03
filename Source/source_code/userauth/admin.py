from django.contrib import admin
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device,UploadFile
admin.site.register(UserProfile)
admin.site.register(UploadAdvetisement)
admin.site.register(Add_Device)
admin.site.register(UploadFile)
# Register your models here.

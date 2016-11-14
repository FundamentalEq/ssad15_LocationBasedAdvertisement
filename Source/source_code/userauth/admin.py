from django.contrib import admin
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device,UploadFile
#models registered on admin
admin.site.register(UserProfile) #it contains PRofile of each user
admin.site.register(Add_Device) # to add device login details

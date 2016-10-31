from django import forms
from django.forms import extras
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device
from django.contrib.admin.widgets import AdminDateWidget

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
   	class Meta:
        	model = User
        	fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    	class Meta:
        	model = UserProfile
        	fields = ('phone_number','address','first_name' , 'last_name', 'ad_type','city','pincode',)
class UploadForm(forms.ModelForm):
	class Meta:
		model = UploadAdvetisement
		fields = ('upload_Advertisement','time_of_advertisement'
		   		,'no_of_slots','select_bundles','no_of_weeks','bussinessPoint_longitude'
				,'bussinessPoint_latitude','start_week','uploader','no_of_repeats',)
		widgets = {'start_week':extras.SelectDateWidget()}
class  Login_Adver(forms.ModelForm):
    class Meta:
		model = Add_Device
		fields = ('Username','password')
		widgets = {'password': forms.PasswordInput(),}

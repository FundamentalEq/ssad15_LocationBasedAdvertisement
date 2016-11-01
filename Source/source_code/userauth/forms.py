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
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First-Name'}),
	    'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email-Id'}),
	    }
        	fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    	class Meta:
        	model = UserProfile
		widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First-Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
	    'address': forms.Textarea(attrs={'class': 'form-control'}),
   	    'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
	    }
        	fields = ('phone_number','address','first_name' , 'last_name', 'ad_type','city','pincode',)
class UploadForm(forms.ModelForm):
	class Meta:
		model = UploadAdvetisement
		fields = ('upload_Advertisement','time_of_advertisement'
		   		,'no_of_slots','select_bundles','no_of_weeks','start_week','uploader','no_of_repeats',)
		widgets = {'start_week':extras.SelectDateWidget(),
		'start_week': forms.DateInput(attrs={'class':'form-control'}),
		'uploader': forms.Select(attrs={'class': 'form-control'}),
		#'upload_Advertisement': forms.FileInput(attrs={'class':'btn btn-default'}),
		'time_of_advertisement': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_slots': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_repeats': forms.NumberInput(attrs={'class': 'form-control'}),
		}
class  Login_Adver(forms.ModelForm):
    class Meta:
		model = Add_Device
		fields = ('Username','password')
		widgets = {'password': forms.PasswordInput(),}

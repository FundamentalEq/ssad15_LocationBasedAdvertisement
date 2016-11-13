from django import forms
from django.contrib import auth
from django.forms import extras
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device,UploadFile
from django.contrib.admin.widgets import AdminDateWidget
import re
import string
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(),validators=[RegexValidator(regex='^[A-Za-z0-9@#$%^&+=]{8,}', message="Password should be a combination of Alphabets and Numbers and atleat 8 digit long",code='invalid_password'),])
	password_confirm = forms.CharField(widget=forms.PasswordInput())
   	class Meta:
        	model = User
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'User-Name'}),
	    'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email-Id'}),
	    }
        	fields = ('username','password','email')
        def clean(self):
                cleaned_data = super(UserForm, self).clean()
                password = cleaned_data.get("password")
                confirm_password = cleaned_data.get("password_confirm")
                if password != confirm_password:
                        raise forms.ValidationError(
                                "password and confirm password does not match"
                )
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		widgets = {
				'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First-Name'}),
				'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last-Name'}),
				'address': forms.Textarea(attrs={'class': 'form-control','placeholder':'Address' }),
				'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter 10 digit phone number'}),
				'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter the city where you do bussiness'}),
				'pincode': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter the pincode of your area'}),
				}
		fields = ('phone_number','address','first_name' , 'last_name', 'ad_type','city','pincode',)


class UploadForm(forms.ModelForm):
	class Meta:
		model = UploadAdvetisement
		fields = ('time_of_advertisement'
		   		,'no_of_slots','select_bundles','no_of_weeks','start_week','uploader','no_of_repeats','bussinessPoint_latitude','bussinessPoint_longitude',)
		widgets = {'start_week':extras.SelectDateWidget(),

		'uploader': forms.Select(attrs={'class': 'form-control'}),
		#'upload_Advertisement': forms.FileInput(attrs={'class':'btn btn-default'}),
		'time_of_advertisement': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_slots': forms.NumberInput(attrs={'class': 'form-control'}),
		'no_of_repeats': forms.NumberInput(attrs={'class': 'form-control'}),
		'select_bundles': forms.NumberInput(attrs={'class': 'form-control'}),
		'bussinessPoint_latitude' : forms.HiddenInput ,
		'bussinessPoint_longitude' : forms.HiddenInput ,
		}

class UploadFileForm(forms.ModelForm):
        class Meta:
                model = UploadFile
                fields = ('upload_Advertisement',)
                widgets = {
                 'upload_Advertisement': forms.FileInput(attrs={'class':'btn btn-default'}),
                }
class  Login_Adver(forms.ModelForm):
    class Meta:
		model = Add_Device
		fields = ('Username','password')
		widgets = {'password': forms.PasswordInput(),}

class UploadForm1(forms.ModelForm):
        class Meta:
                model = UploadAdvetisement
                fields = ('time_of_advertisement'
                                ,'no_of_slots','select_bundles','no_of_weeks','start_week','no_of_repeats','bussinessPoint_latitude','bussinessPoint_longitude',)
                widgets = {'start_week':extras.SelectDateWidget(),

                #'upload_Advertisement': forms.FileInput(attrs={'class':'btn btn-default'}),
                'time_of_advertisement': forms.NumberInput(attrs={'class': 'form-control'}),
                'no_of_weeks': forms.NumberInput(attrs={'class': 'form-control'}),
                'no_of_slots': forms.NumberInput(attrs={'class': 'form-control'}),
                'no_of_repeats': forms.NumberInput(attrs={'class': 'form-control'}),
                'select_bundles': forms.NumberInput(attrs={'class': 'form-control'}),
                'bussinessPoint_latitude' : forms.HiddenInput ,
                'bussinessPoint_longitude' : forms.HiddenInput ,
                }

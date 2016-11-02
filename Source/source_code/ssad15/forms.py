from django import forms
from django.forms import extras
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device
from django.contrib.admin.widgets import AdminDateWidget
import datetime
class zone_info_form(forms.Form) :
    week = forms.DateField(initial=datetime.date.today)
    cost = forms.IntegerField(initial=100)
    no_of_bundles = forms.IntegerField(initial=10)
    widgets = {'week':extras.SelectDateWidget(),
    'week': forms.DateInput(attrs={'class':'form-control'}),}

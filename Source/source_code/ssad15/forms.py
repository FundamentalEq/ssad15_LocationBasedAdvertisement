from django import forms
from django.forms import extras
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from userauth.models import UserProfile
from userauth.models import UploadAdvetisement,Add_Device
from django.contrib.admin.widgets import AdminDateWidget
from global_values import *
class zone_info_form(forms.Form) :
    week = forms.DateField(widget=extras.SelectDateWidget)
    cost = forms.IntegerField(initial=DEFAULT_COST)
    no_of_bundles = forms.IntegerField(initial=DEFAULT_BUNDLES)
    # widgets = {'week':extras.SelectDateWidget(),}

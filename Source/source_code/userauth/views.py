from django.shortcuts import render
from django.template import RequestContext
from django.template import context
from models import Add_Device
from django.shortcuts import render_to_response
from userauth.forms import UserForm, UserProfileForm, UploadForm, UploadFileForm, UploadForm1
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from ssad15.views import check_availability
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from userauth.models import UserProfile, UploadAdvetisement, UploadFile
import math
from global_values import *
from ssad15.views import *
from ssad15.views import check_availability as checkavailable
from ssad15.views import total_cost as cost
import os
import zipfile
import StringIO
import itertools
from django.contrib.auth.models import UserManager
def register(request):

	registered = False
	val = 0
    	if request.method == 'POST':
        	user_form = UserForm(data=request.POST)
        	profile_form = UserProfileForm(data=request.POST)

        	if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirm']:
            		user = user_form.save(commit=False)
                        profile = profile_form.save(commit=False)
			if User.objects.filter(email = user.email).count()>=1:
                                val = 1
			else:
            			user.set_password(user.password)
            			user.save()
            			profile.user = user
                        	profile.save()
				registered = True


        	else:
            		print user_form.errors , profile_form.errors

    	else:
        	user_form = UserForm()
        	profile_form = UserProfileForm()

    	return render(request,'userauth/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'val': val,})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/userauth/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'userauth/login.html', {})

@login_required
def restricted(request):
	 return HttpResponse("Since you're logged in, you can see this text!")
def user_logout(request):
    	logout(request)
	return HttpResponseRedirect('/userauth/')
	#return render(request,'userauth/base.html', {})
'''
def upload(request):
	global uploaded
	uploaded = False
	msg = "sending nothing"
	val = 0
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			global post
			post = form.save(commit=False)
			if not checkavailable(post):
                        	val = 1
                        else:
<<<<<<< HEAD
				global c
			       	val = 2
                               	c = cost(post)
                               	post.amount_paid = c
			       	if not request.user.is_superuser:
                               		post.uploader = request.user
			       	post.no_of_slots = math.ceil((post.no_of_repeats*post.time_of_advertisement)/30.0)
			       	p = UploadFileForm()
			       	return render(request,'userauth/total_cost.html',{'p': p ,'c':c,})
=======
			       global c
			       val = 2
                               c = cost(post)
                               post.amount_paid = c
			       if not request.user.is_superuser:
                               	post.uploader = request.user
			       post.no_of_slots = math.ceil((post.no_of_repeats*post.time_of_advertisement)/30.0)
			       p = UploadFileForm()
			       return render(request,'userauth/total_cost.html',{'p': p ,'c':c,})
>>>>>>> f5e3affb22da1e92f2a334be45e2fb12c5fa097c
		else:
			print form.errors
	else :
		form = UploadForm()
	return render(request,'userauth/upload.html', {'form': form , 'uploaded':uploaded ,'msg':msg ,  'val':val,})
'''
def upload(request):
        if  request.user.is_superuser:
                global uploaded
                uploaded = False
                msg = "sending nothing"
                val = 0
                if request.method == "POST":
                        form = UploadForm(request.POST, request.FILES)
                        if form.is_valid():
                                global post
                                post = form.save(commit=False)
                                if not checkavailable(post):
                                        val = 1
                                else:
                                        global c
                                        val = 2
                                        c = cost(post)
                                        post.amount_paid = c
                                        if not request.user.is_superuser:
                                                post.uploader = request.user
                                        post.no_of_slots = math.ceil((post.no_of_repeats*post.time_of_advertisement)/30.0)
                                        p = UploadFileForm()
                                        return render(request,'userauth/total_cost.html',{'p': p ,'c':c,})
                        else:
                                print form.errors
                else :
                        form = UploadForm()
                return render(request,'userauth/upload.html', {'form': form , 'uploaded':uploaded ,'msg':msg ,  'val':val,})
        else:
                global uploaded
                uploaded = False
                msg = "sending nothing"
                val = 0
                if request.method == "POST":
                        form = UploadForm1(request.POST, request.FILES)
                        if form.is_valid():
                                global post
                                post = form.save(commit=False)
                                if not checkavailable(post):
                                        val = 1
                                else:
                                        global c
                                        val = 2
                                        c = cost(post)
                                        post.amount_paid = c
                                        if not request.user.is_superuser:
                                                post.uploader = request.user
                                        post.no_of_slots = math.ceil((post.no_of_repeats*post.time_of_advertisement)/30.0)
                                        p = UploadFileForm()
                                        return render(request,'userauth/total_cost.html',{'p': p ,'c':c,})
                        else:
                                print form.errors
                else :
                        form = UploadForm1()
                return render(request,'userauth/upload.html', {'form': form , 'uploaded':uploaded ,'msg':msg ,  'val':val,})

def home(request):
	return render(request,'userauth/index.html')
def device_login(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                #if Add_Device.objects.filter(Username=request.POST['username'], password=request.POST['password']).exists():
                if Add_Device.objects.filter(Username=request.POST['username'],password=request.POST['password']).count()==1:
                        #return render(request,'/userauth/')
                        return HttpResponseRedirect('/ssad15/start_advertisement')
                else:
                        return HttpResponse("Invalid Login")
        else:
                return render(request,'userauth/logdiv.html', {})
def user_edit(request,pk):
        if UserProfile.objects.filter(user = request.user).count()==1:
                print 11
		Edit = 0
                user = request.user
                userprofile = get_object_or_404(UserProfile , user=user)
                if request.method == "POST":
			print 22
                        user_form = UserForm(data=request.POST , instance=user)
                        profile_form = UserProfileForm(data=request.POST , instance = userprofile)
                        if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirm']:
                                Edit = 1
				user = user_form.save()
                        	user.set_password(user.password)
                        	user.save()
                        	profile = profile_form.save(commit=False)
                        	profile.user = user
                        	profile.save()
                                login(request, user)
                else:
                        user_form = UserForm(instance=user)
                        profile_form = UserProfileForm(instance=userprofile)
		print 33
                return render(request, 'userauth/register_edit.html', {'user_form': user_form, 'profile_form': profile_form, 'Edit':Edit})
        else:
                Edit = 2
                user = request.user
                if request.method == "POST":
                        user_form = UserForm(data=request.POST , instance=user)
                        if user_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['password_confirm'] :
                                Edit = 3
                                user = user_form.save()
                        	user.set_password(user.password)
				user.save()
				login(request, user)
                else:
                        user_form = UserForm(instance=user)
                return render(request, 'userauth/register_edit.html', {'user_form': user_form, 'Edit':Edit})
def user_history(request):
	if  request.user.is_superuser:
        	advertisment = UploadAdvetisement.objects.all().order_by('-uploader')
		ads = UploadFile.objects.all().order_by('-date')
	else:
        	advertisment = UploadAdvetisement.objects.filter(uploader = request.user).order_by('-date')
		ads = UploadFile.objects.filter(uploader = request.user).order_by('-date')
        return render(request, 'userauth/user_history.html', {'advertisment':advertisment , 'ads':ads})

# auto complete feature that help selects the username
# class autocompleteUser(autocomplete.Select2QuerySetView) :
# 	def get_queryset(self):
# 		if not self.request.user.is_superuser:
# 			return User.objects.none()
# 		qs = User.objects.all()
# 		if self.q :
# 			qs = qs.filter(email__istartswith=self.q)
# 		return qs
            # return auth.User.objects.none()


def total_cost(request):
	if request.method == "POST":
		p = UploadFileForm(request.POST, request.FILES)
                if p.is_valid():
                        p = p.save(commit=False)
                        if  request.user.is_superuser:
                                p.uploader = post.uploader
                        else:
                                p.uploader = request.user
			post.save()
                	p.uploadby = post
                	p.save()
                        return render(request,'userauth/thanks.html', {})
	else:
		p = UploadFileForm()
	return render(request,'userauth/total_cost.html',{'p': p ,'c':c})
def not_confirm_cost(request):
	return render(request,'userauth/nothanks.html', {})

def upload_advertisement(request):
	if request.user.is_authenticated:
		return redirect(upload)
	else:
		return redirect(login)

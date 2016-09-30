from django.shortcuts import render
from django.template import RequestContext
from django.template import context
from django.shortcuts import render_to_response
from userauth.forms import UserForm, UserProfileForm, UploadForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def register(request):

	registered = False

    	if request.method == 'POST':
        	user_form = UserForm(data=request.POST)
        	profile_form = UserProfileForm(data=request.POST)

        	if user_form.is_valid() and profile_form.is_valid():
            		user = user_form.save()

            		user.set_password(user.password)
            		user.save()

            		profile = profile_form.save(commit=False)
            		profile.user = user


            		profile.save()

            		registered = True
                 
       
        	else:
            		print user_form.errors, profile_form.errors

    	else:
        	user_form = UserForm()
        	profile_form = UserProfileForm()

    	return render(request,'userauth/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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

def upload(request):
	uploaded = False
        if request.method == "POST":
           form = UploadForm(request.POST, request.FILES)
           if form.is_valid():
            	post = form.save(commit=False)
            	post.uploader = request.user
            	uploaded = True
            	post.save()
            	
	else:
		form = UploadForm()
	return render(request,'userauth/upload.html', {'form': form , 'uploaded':uploaded})
	

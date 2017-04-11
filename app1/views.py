from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect	
from .forms import ChangepwdForm, DocumentForm
from login.models import LoginDetails
from app1.models import Document
from django.views.decorators.cache import cache_control
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userhome(request):
	try:
		username = request.session['username']
		designation = request.session['access']
		clientid = request.session['clientid']
		levels = ['public','private','confidential','topsecret']
		context = {
		'username' : username,
		'designation' : levels[designation%4 - 1],
		'nbar' : 'home',
		}
	except:
		return HttpResponseRedirect('/')
	if designation == 5:
		del request.session['username']
		return HttpResponseRedirect('/')
	return render(request, 'app1/userHome.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def detectorhome(request):
	try:
		username = request.session['username']
		designation = request.session['access']
		clientid = request.session['clientid']
		context = {
		'username' : username,
		'nbar' : 'home',
		}
	except:
		return HttpResponseRedirect('/')
	if designation != 5:
		del request.session['username'] #end the session
		return HttpResponseRedirect('/') #redirect to login page	
	return render(request, 'app1/detectorHome.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(request):
	try:
		username = request.session['username']
		designation = request.session['access']
		clientid = request.session['clientid']
	except:
		return HttpResponseRedirect('/')
	levels = ['public','private','confidential','topsecret']	
	if request.method == 'POST':
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			current = form.cleaned_data['current']
			new = form.cleaned_data['new']
			reenter = form.cleaned_data['reenter']

			q = LoginDetails.objects.get(clientid=clientid)
			if q.password == current:
				if new == reenter:
					q.password = new
					q.save()
				else:
					return HttpResponse("new and reentered password doesn't match")
			else:
				return HttpResponse("incorrect password")
	else:
		form = ChangepwdForm()

	context = {
		'form' : form,
		'username' : username,
		'designation' : levels[designation%4 -1],
		'nbar' : 'changepass'
	}
	if designation == 5:
		return render(request, 'app1/detector_changePassword.html', context)
	else:
		return render(request, 'app1/user_changePassword.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def modelformupload(request):
	try:
		username = request.session['username']
		designation = request.session['access']
	except:
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			if request.POST['accesslevel'] > str(designation):
				return HttpResponse("Access level not allowed")
			else:
				form.save()
			return HttpResponseRedirect('/user/userhome')
	else:
		form = DocumentForm()
	levels = ['public', 'private', 'confidential', 'topsecret']
	context = {
		'form' : form,
		'designation': levels[designation%4 -1],
		'nbar':'uploaddoc',
		'username' : username,
	}
	return render(request, 'app1/user_uploadDocument.html', context)
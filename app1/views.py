from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect	
from .forms import ChangepwdForm
from login.models import LoginDetails
# Create your views here.
def userhome(request):
	username = request.session['username']
	designation = request.session['access']
	clientid = request.session['clientid']
	levels = ['public','private','confidential','topsecret']
	context = {
	'username' : username,
	'designation' : levels[designation%4 - 1]

	}
	return render(request, 'app1/userHome.html', context)

def detectorhome(request):
	username = request.session['username']
	designation = request.session['access']
	clientid = request.session['clientid']
	if designation != 5:
		del request.session['username'] #end the session
		return HttpResponseRedirect('/') #redirect to login page
	context = {
	'username' : username,
	}
	return render(request, 'app1/detectorHome.html', context)

def displaychangepwd(request):
	designation = request.session['access']
	return HttpResponseRedirect('/user/changepassword/')

def changepassword(request):
	username = request.session['username']
	designation = request.session['access']
	clientid = request.session['clientid']
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
		'designation' : levels[designation%4 -1]
	}
	if designation ==5:
		return render(request, 'app1/detector_changePassword.html', context)
	else:
		return render(request, 'app1/user_changePassword.html', context)
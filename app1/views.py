from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect	
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
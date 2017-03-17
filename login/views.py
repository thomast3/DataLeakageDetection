from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginDetailsForm
from .models import LoginDetails
# Create your views here.

def login_form(request):
	if request.method == 'POST':
		form = LoginDetailsForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			try:
				q = LoginDetails.objects.get(username=username)
				if(q.password == password):
					return HttpResponse("<h1> Access Granted </h1>")
				else:
					return HttpResponse("<h1> Access Denied </h1>")
			except:
				return HttpResponse("<h1> Access Denied </h1>")
	else:
		form = LoginDetailsForm()
	return render(request, 'login/index.html', {'form':form})
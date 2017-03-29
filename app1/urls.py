from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^userhome', views.userhome),
	url(r'^detectorhome', views.detectorhome),
	url(r'^changepassword', views.changepassword),
]
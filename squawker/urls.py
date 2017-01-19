from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'squawker'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-squawk/', views.add_squawk, name='index'), 
	url(r'^admin/', admin.site.urls),
	]

from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


app_name = 'squawker'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-squawk/', views.add_squawk, name='index'), 
	url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	]

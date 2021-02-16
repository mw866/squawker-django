from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = 'squawker'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-squawk/', views.add_squawk, name='index'), 
	url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView, name='login'),
	url(r'^logout/$', auth_views.LogoutView, {'next_page': '/'}, name='logout'),

	url(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('favicon.ico'), permanent=False),
        name="favicon"
    ),
	]

from django.urls import path

from . import views

app_name = 'siteapp'
urlpatterns = [
    path('', views.siteapp, name='site_home'),
]

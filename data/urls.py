__author__ = 'Adam Thomson'
from django.conf.urls import patterns, url
from data import views

urlpatterns = patterns('',
    # /index/
    url(r'^$', views.index, name='index'),
    # /doctors/
    url(r'^users/$', views.doctors, name = 'users'),
    # /doctors/123/
    url(r'^users/(?P<badge_id>\w+)/$', views.doctor_details, name = 'user_details'),
    # /stations/
    url(r'^nodes/$', views.stations, name = 'nodes'),
    # /stations/27/
    url(r'^nodes/(?P<station_id>\d+)/$', views.station_details, name = 'node_details'),
    # /washings/
    url(r'^events/$', views.washings, name = 'events'),
    # /washings/123
    url(r'^events/(?P<wash_id>\d+)/$', views.washing_details, name = 'event_details')
)

__author__ = 'Adam Thomson'
from django.conf.urls import patterns, url
from data import views

urlpatterns = patterns('',
    # /index/
    url(r'^$', views.index, name='index'),
    # /users/
    url(r'^users/$', views.users, name = 'users'),
    # /users/123/
    url(r'^users/(?P<badge_id>\w+)/$', views.user_details, name = 'user_details'),
    # /nodes/
    url(r'^nodes/$', views.nodes, name = 'nodes'),
    # /nodes/27/
    url(r'^nodes/(?P<station_id>\d+)/$', views.node_details, name = 'node_details'),
    # /events/
    url(r'^events/$', views.events, name = 'events'),
    # /events/123
    url(r'^events/(?P<wash_id>\d+)/$', views.event_details, name = 'event_details')
)

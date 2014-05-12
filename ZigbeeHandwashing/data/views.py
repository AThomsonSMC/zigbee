from django.shortcuts import render
from django.http import HttpResponse
from data.models import Users, Networks, Nodes, Events

def index(request):
    return HttpResponse("Welcome to the index!")

def users(request):
    return HttpResponse("You're looking at the list of users.")

def networkd(request):
    return HttpResponse("You're looking at the list of networks.")

def nodes(request):
    return HttpResponse("You're looking at the list of nodes.")

def events(request):
    return HttpResponse("You're looking at the list of events.")

def user_details(request, badge_id):
    return HttpResponse("You're looking at the details of user %s." % badge_id)

def network_details(request, net_id):
    return HttpResponse("You're looking at the details of network %s." % net_id)

def node_details(request, node_id):
    return HttpResponse("You're looking at the details of node %s." % node_id)

def event_details(request, event_id):
    return HttpResponse("You're looking at the details of event %s." % event_id)
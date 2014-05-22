from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from data.models import Users, Networks, Nodes, Events

def index(request):
    user_list = Users.objects.order_by('-name_last').values('badge_id')
    latest_list = {}
    for u in user_list:
        latest_list[u[0]] = get_latest_event(u[0])
    template = loader.get_template('data/index.html')
    context = RequestContext(request,{
        'latest_list': latest_list,
    })
    return HttpResponse(template.render(context))

def get_latest_event(user_id):
    qs = Events.objects.filter(user__badge_id=user_id).order_by('timestamp')
    last = qs[0]
    return last

def users(request):
    return HttpResponse("You're looking at the list of users.")

def networks(request):
    return HttpResponse("You're looking at the list of networks.")

def nodes(request):
    return HttpResponse("You're looking at the list of nodes.")

def events(request):
    return HttpResponse("You're looking at the list of events.")

def user_details(request, badge_id):
    try:
        user = Users.objects.filter(badge_id=badge_id)
    except Users.DoesNotExist:
        raise Http404
    return render(request, 'data/user_details.html', {'user': user})

def network_details(request, network_id):
    try:
        network = Networks.objects.filter(net_id=network_id)
    except Users.DoesNotExist:
        raise Http404
    return render(request, 'data/network_details.html', {'net': network})

def node_details(request, node_id):
    try:
        node = Nodes.objects.filter(node_id=node_id)
    except Users.DoesNotExist:
        raise Http404
    return render(request, 'data/node_details.html', {'node': node})

def event_details(request, event_id):
    try:
        event = Events.objects.filter(event_id=event_id)
    except Users.DoesNotExist:
        raise Http404
    return render(request, 'data/event_details.html', {'event': event})
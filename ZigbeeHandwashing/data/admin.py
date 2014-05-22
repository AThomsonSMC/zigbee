from django.contrib import admin
from data.models import Users, Networks, Nodes, Events

class EventInline(admin.TabularInline):
    date_hierarchy = 'timestamp'
    model = Events
    extra = 1

class UserAdmin(admin.ModelAdmin):
    fields = ['badge_id', 'name_first', 'name_last']
    list_filter = ['badge_id','name_first', 'name_last']
    search_fields = ['badge_id','name_first', 'name_last']

class NodeAdmin(admin.ModelAdmin):
    fields = ['node_id', 'networks', 'name']
    list_filter = ['node_id', 'name']
    search_fields = ['node_id','name']

class NetworkAdmin(admin.ModelAdmin):
    fields = ['net_id', 'name', 'ip_add']
    list_filter = ['net_id', 'name', 'ip_add']
    search_fields = ['net_id', 'name', 'ip_add']

admin.site.register(Users, UserAdmin)
admin.site.register(Nodes, NodeAdmin)
admin.site.register(Networks, NetworkAdmin)
from django.db import models
import datetime

BATTERY_WARNING = .15
BATTERY_CRITICAL = .05
SOAP_WARNING = .25
SOAP_CRITICAL = .1

class Users(models.Model):
    badge_id = models.CharField(max_length = 16, unique=True)
    name_first = models.CharField(max_length = 200)
    name_last = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 10)
    #in_compliance = models.CharField(max_length = 1, choices=[('Y','Yes'),('N','No'),('A','N/A')])

    #def is_in_compliance(self, in_compliance):
    #    if in_compliance == 'Y': return True
    #    if in_compliance == 'N': return False
    #    if in_compliance == 'A': return True
    #    else: return False
    #is_in_compliance.boolean = True
    #is_in_compliance.short_description = 'Washed hands today?'

    def __str__(self):
        return "Badge: %s, Name: %s, %s" % (self.badge_id, self.name_last, self.name_first)


class Networks(models.Model):
    net_id = models.CharField(max_length = 200, unique=True)
    name = models.CharField(max_length = 200)
    port = models.IntegerField(max_length = 4, default = 0)
    ip_add = models.CharField(max_length = 16)
    status = models.CharField(max_length = 50)
    def __str__(self):
        return "Network: %s, IP: %s" % (self.name, self.ip_add)


class Nodes(models.Model):
    node_id = models.CharField(max_length = 16, unique=True)
    name = models.TextField(max_length = 200)
    type = models.CharField(max_length = 200)
    soap_level = models.FloatField(default = 0.0)
    battery_level = models.FloatField(default = 0.0)
    networks = models.ForeignKey(Networks)
    loc_x = models.FloatField(default = 0)
    loc_y = models.FloatField(default = 0)
    loc_z = models.FloatField(default = 0)
    def __str__(self):
        return "ID: %s, Name: %s" % (self.node_id, self.name)
    def battery_alert(self):
        if self.battery_level < BATTERY_WARNING:
            #send alert
            pass
        if self.battery_level < BATTERY_CRITICAL:
            #send high priority alert
            pass
    def soap_alert(self):
        if self.soap_level < SOAP_WARNING:
            #send alert
            pass
        if self.soap_level < SOAP_CRITICAL:
            #send high priority alert
            pass


class Events(models.Model):
    event_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(Users)
    timestamp = models.DateTimeField(default = datetime.datetime.now())
    node = models.ForeignKey(Nodes)
    type = models.CharField(max_length = 200)
    data = models.TextField(max_length = 1000)
    def __str__(self):
        return "User: %s, %s - Time: %s" % (self.user.name_last, self.user.name_first, self.timestamp)
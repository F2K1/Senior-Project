from django.db import models
from django.contrib.auth.models import User


#"Tenant" table
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=400, null=False, default="undefined")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " (" + self.user.username + ")" 


#"Landlord" table
class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=400, null=False, default="undefined")
    phone2 = models.CharField(max_length=400, null=True)
    iban = models.CharField(max_length=34, null=False, default="undefined")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " (" + self.user.username + ")" 


#"Property" table
class Property(models.Model):
    RESIDENCE = 'residence'
    FLAT = 'flat'
    ROOM = 'room'

    PROPERTY_TYPES = {
        (RESIDENCE, 'Residence'),
        (FLAT, 'Flat'),
        (ROOM, 'Room'),
    }

    UN = 'Undefined'
    BR = 'Brno'
    PR = 'Prague'
    TR = 'Tirana'
    CITY_LIST = {
        (UN, 'undefined'),
        (BR, 'brno-czech_republic'),
        (PR, 'prague-czech_republic'),
        (TR, 'tirana-albania'),
    } 

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False, default="undefined")
    type = models.CharField(max_length=9, choices=PROPERTY_TYPES, default=ROOM, null=False)
    size = models.IntegerField(null=False, default=0)
    city = models.CharField(max_length=50, choices=CITY_LIST, default=UN, null=False)
    address = models.CharField(max_length=400)
    price = models.IntegerField(null=False, default=0)
    img = models.IntegerField(null=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=False, default=0, blank=True)
    
    def __str__(self):
        return self.name + " (" + self.address + ")"


#"Rental" table
class Rental(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False, default=0, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.property.name + " (" + self.property.address + ")"
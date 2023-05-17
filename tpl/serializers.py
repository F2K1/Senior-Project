from rest_framework import serializers
from django.contrib.auth.models import User
from tpl.models import Landlord, Tenant, Property, Rental


#"User" json translator
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username',
                 'email',)

#"Tenant" json translator
class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('phone',)

#"Landlord" json translator
class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = ('phone',
                  'phone2',
                  'iban',)

#"Property" json translator 
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('name',
                  'type',
                  'size',
                  'city',
                  'address',
                  'price',
                  'img',
                  'landlord',)
        
#"Rental" json translator
class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('start_date',
                  'end_date',
                  'property',
                  'tenant',)
        

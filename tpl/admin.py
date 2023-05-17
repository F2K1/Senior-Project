from django.contrib import admin
from tpl.models import Tenant, Landlord, Property, Rental


admin.site.register(Tenant)
admin.site.register(Landlord)
admin.site.register(Property)
admin.site.register(Rental)
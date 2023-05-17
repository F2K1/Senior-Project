from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from tpl.models import Tenant, Landlord, Property, Rental
from tpl.serializers import UserSerializer, TenantSerializer, LandlordSerializer, PropertySerializer, RentalSerializer


#"Landlord" api
def requestLandlord(request):
    pass


#"Tenant" api
def requestTenant(request):
    pass


#"User" api
#signin user
@csrf_exempt
def signinUser(request):
    if request.method == "POST":
        user_data = json.loads(request.body)
        username_list = User.objects.values_list("username", flat=True) 
        email_list = User.objects.values_list("email", flat=True)
        
        if user_data["username"] in username_list:
            return JsonResponse({"response": "Username is already taken. Please use another alias"})
        
        elif user_data["email"] in email_list:
            return JsonResponse({"response": "Email account is already in use. Please use another email account"})
        
        elif user_data["username"] in username_list and user_data["email"] in email_list:
            return JsonResponse({"response": "Username and email account are already in use. Please use another username and email account"})
        
        else:
            new_user = User.objects.create_user(username=user_data["username"], first_name=user_data["firstname"], last_name=user_data["lastname"], email=user_data["email"], password=user_data["password"])
            new_user.save()
            if user_data["usertype"] == "tenant":
                new_tenant = Tenant(user=new_user, phone=user_data["prefix1"] + " " + user_data["phone1"])
                new_tenant.save()
                return JsonResponse({"response": "Account created"})
            
            elif user_data["usertype"] == "landlord":
                if user_data["phone2"] != "null":
                    new_landlord = Landlord(user=new_user.id, phone=user_data["prefix1"] + " " + user_data["phone1"], phone2=user_data["prefix2"] + " " + user_data["phone2"], iban=user_data["iban"])   
                    new_landlord.save()
                    return JsonResponse({"response": "Account created"})
                else:
                    new_landlord = Landlord(user=new_user.id, phone=user_data["prefix1"] + " " + user_data["phone1"], iban=user_data["iban"])
                    new_landlord.save()
                    return JsonResponse({"response": "Account created"})
                

#login user
@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        pass


#"Property" api
#select all properties
def requestProperties(request):
    if request.method == "GET":
        properties = Property.objects.all()
        properties = PropertySerializer(properties, many=True)
        return JsonResponse(properties.data, safe=False)
    
def requestProperty(request, id):
    if request.method == "GET":
        property = Property.objects.get(id=id)
        property = PropertySerializer(property, many=False)
        return JsonResponse(property.data, safe=False)

#"Rental" api
def requestRental(request):
    if request.method == "GET":
        rentals = Rental.objects.all()
        rentals = RentalSerializer(rentals, many=True)
        return JsonResponse(rentals.data, safe=False)



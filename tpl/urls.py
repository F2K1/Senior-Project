from django.urls import re_path
import tpl.views as views


urlpatterns= [
    #"Property" links
    re_path('^on-sale/', views.requestProperties),
    re_path('^show/(?P<id>\d+)/', views.requestProperty),
    re_path('^rentals/', views.requestProperties),
    
    #"User" links
    re_path('^signin/', views.signinUser),
    re_path('^login/', views.loginUser),
]
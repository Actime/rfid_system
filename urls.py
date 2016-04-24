# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 5, 2016
"""
# Imports
from django.conf.urls import include, url
from django.contrib import admin
import regbackend

# General Url patterns
urlpatterns = [
    
    url( r'^admin/', include(admin.site.urls)),
    # Index view
    url( r'^$', 'events.views.index', name='views.index' ),
    url( r'^contact/$', 'events.views.contact', name='views.contact' ),
    url( r'^about/$', 'events.views.about', name='views.about' ),
    # Accoutns urls
    url( r'^accounts/register/$', regbackend.CustomRegistrationView.as_view(), name='registration_register'),
    url( r'^accounts/', include('registration.backends.default.urls')),
    # Api urls
    url( r'^api/', include('api.urls')),
    # Events modules urls
    url( r'^event/', include('events.urls')),
    # Competitors module urls
    url( r'^competitor/', include('competitors.urls')),
    # The facebook shit
    url( r'^facebook/', include('django_facebook.urls')),
    url( r'^accounts/', include('django_facebook.auth_urls')),
    
]# End of general sytem url patterns
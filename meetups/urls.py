from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index),  # our-domain.com/meetups
    path('meetup/<slug:meetup_slug>', views.meetup_details) # our-domain.com/meetups/<meetup_slug>
]

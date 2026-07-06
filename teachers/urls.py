from django.urls import path
from .views import *



urlpatterns = [
    path('', all_teachers),
    path('backend/', backend_teachers),
    path('frontend/', frontend_teachers),
    path('mobile/', mobile_teachers),
    path('contact/', contact_)
]














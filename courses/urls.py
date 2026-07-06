from django.urls import path
from .views import *


urlpatterns = [
    path('', all_courses),
    path('backend/', backend_courses),
    path('frontend/', frontend_courses),
    path('mobile/', mobile_course),
    path('prices/', prices)
]

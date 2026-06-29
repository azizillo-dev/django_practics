from django.urls import path
from .views import *
    





urlpatterns = [
    path('', all_students),
    path('top/', top),
    path('graduated/', graduated_st),
    path("<int:id>/", get_student),
    path("city/<str:city>/",students_by_city)

]




from django.urls import path
from .views import calculate_trip_cost

urlpatterns = [
    path('', calculate_trip_cost, name='calculate_trip_cost'),
]
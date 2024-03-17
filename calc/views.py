from django.shortcuts import render
from .forms import TripForm
from .models import Trip

def calculate_trip_cost(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            # Calculate total cost
            total_cost = trip.distance * trip.price_for_km
            if trip.toll_road:
                total_cost += trip.toll_road_cost
            trip.total_cost = total_cost  # Assuming 'total_cost' is a field in the Trip model
            trip.save()
            return render(request, 'calc/calculate_trip.html', {'trip': trip, 'trip_cost': total_cost})
    else:
        form = TripForm()
    return render(request, 'calc/calculate_trip.html', {'form': form})

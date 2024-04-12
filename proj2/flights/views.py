from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight,Passenger,Airport

def add_passenger(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        # Extract passenger data from POST request
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        flight_id = request.POST.get('flight')
        
        try:
            # Create passenger instance
            passenger = Passenger.objects.create(
                first=first_name,
                last=last_name
            )
            
            # Add passenger to flight
            flight = Flight.objects.get(pk=flight_id)
            passenger.flights.add(flight)
            
            # Redirect to a success page or another URL
            return render(request, 'flights/add_passenger.html', 
                          {'message': "Passenger Successfully Added"})
        except Exception as e:
            # Handle any errors
            error_message = str(e)
            return render(request, 'flights/add_passenger.html', 
                          {'message': "Passenger Not Added"})
    else:

        flights = Flight.objects.all()
  
        return render(request, 'flights/add_passenger.html', {'flights': flights})

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passenger":Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == "POST":
        flight =Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passanger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight:flight",args=(flight_id,)))
    
def add_airport(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        code = request.POST.get('code')
        city = request.POST.get('city') 
        try:
            airport = Airport.objects.create(
                code=code,
                city=city
            )
            return render(request, 'flights/add_airport.html',{
                "message":"Airport Successfully Added"
            })
        except Exception as e:
            return render(request, 'flights/add_airport.html', 
                          {'message': "Airport Not Added"})
    else:
        return render(request, 'flights/add_airport.html')
    
def add_flight(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        origin_id = request.POST.get('origin')
        destination_id = request.POST.get('destination')
        duration = request.POST.get('duration')
        
        try:
            # Retrieve origin and destination airports
            origin = Airport.objects.get(pk=origin_id)
            destination = Airport.objects.get(pk=destination_id)
            
            # Create a new Flight object
            flight = Flight.objects.create(
                origin=origin,
                destination=destination,
                duration=duration
            )
            # Redirect to a success page or another URL
            return render(request, 'flights/add_flight.html',{
                "message":"Flight Successfully Added"
            })
        except Exception as e:
            # Handle any errors
            return render(request, 'flights/add_flight.html', 
                          {'message': "Flight Not Added"})
    else:
        # Get all airports from the database
        airports = Airport.objects.all()
        
        # Pass airports to the template context
        return render(request, 'flights/add_flight.html', {'airports': airports})
    
def update_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, pk=passenger_id)
    if request.method == 'POST':
        passenger.first = request.POST.get('first')
        passenger.last = request.POST.get('last')
        passenger.save()
        return render(request, 'flights/update_passenger.html',{
                "message":"Passenger Updated Successfully"
            })
    return render(request, 'flights/update_passenger.html', {'passenger': passenger})

def update_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        flight.origin_id = request.POST.get('origin')
        flight.destination_id = request.POST.get('destination')
        flight.duration = request.POST.get('duration')
        flight.save()
        return render(request, 'flights/update_flight.html',{
                "message":"Flight Updated Successfully"
            })
    return render(request, 'flights/update_flight.html', {'flight': flight})

def update_airport(request, airport_id):
    airport = get_object_or_404(Airport, pk=airport_id)
    if request.method == 'POST':
        airport.code = request.POST.get('code')
        airport.city = request.POST.get('city')
        airport.save()
        return render(request, 'flights/update_airport.html',{
                "message":"Airport Updated Successfully"
            })
    return render(request, 'flights/update_airport.html', {'airport': airport})
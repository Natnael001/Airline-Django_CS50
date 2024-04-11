from django.urls import path

from . import views

app_name = 'flight'
urlpatterns = [
    path("",views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    path('add_passenger/', views.add_passenger, name='add_passenger'),
    path('add_airport/', views.add_airport, name='add_airport'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('update_passenger/', views.update_passenger, name='update_passenger'),
    path('update_airport/', views.update_airport, name='update_airport'),
    path('update_flight/', views.update_flight, name='update_flight'),
]
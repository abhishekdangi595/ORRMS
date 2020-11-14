from django.urls import path
from . import views

urlpatterns = [
    path('flat/', views.add_property_flat, name='flat_insert'),
    path('room/', views.add_property_room, name='room_insert'),
    path('flat/<int:id>/', views.add_property_flat, name='flat_update'),
    path('room/<int:id>/', views.add_property_room, name='room_update'),
    path('Flat_delete/<int:id>', views.flat_delete, name='flat_delete'),
    path('Room_delete/<int:id>', views.room_delete, name='room_delete'),
    path('Flat_details/<int:id>/', views.flat_details, name='property_details'),
    path('Room_details/<int:id>/', views.room_details, name='room_details'),
]

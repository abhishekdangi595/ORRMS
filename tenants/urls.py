from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search_result'),
    path('rent_view', views.rent_view, name='rent_view'),

]
from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('items/', views.items),
    path('items/<int:pk>/', views.item_detail),
    path('restaurants/', views.restaurants),
    path('restaurants/<int:pk>/', views.restaurant_detail),

    # auth0authorization/urls.py
]
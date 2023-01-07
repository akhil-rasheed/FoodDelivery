from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('items/', views.items),
    path('items/<int:pk>/', views.item_detail),

    # auth0authorization/urls.py
]
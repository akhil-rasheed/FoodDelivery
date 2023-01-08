from rest_framework import routers,serializers,viewsets
from .models import Item, Restaurant

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name', 'description', 'image', 'price', 'restaurant']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name', 'image', 'cuisine', 'rating']
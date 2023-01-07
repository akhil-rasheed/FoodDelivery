from rest_framework import routers,serializers,viewsets
from .models import Item, Restaurant

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'price']

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'image', 'cuisine', 'rating']
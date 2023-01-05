from rest_framework import routers,serializers,viewsets
from .models import Item
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'price']
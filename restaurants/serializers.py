from rest_framework import serializers
from .models import Restaurants


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['name', 'location', 'xco', 'yco', 'upinfo', 'downinfo', 'resnumber', 'mainpic', 'menupic', 'respic', 'category']

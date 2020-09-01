from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurants
from .serializers import RestaurantsSerializer


@csrf_exempt
def restaurant_list(request):
    if request.method == 'GET':
        query_set = Restaurants.objects.all()
        serializer = RestaurantsSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

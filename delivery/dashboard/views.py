from django.shortcuts import render

# Create your views here.

# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for item
from .serializers import ItemSerializer, RestaurantSerializer, OrderSerializer
# Item model
from .models import Item, Restaurant, Order

from rest_framework.decorators import api_view
from functools import wraps
import jwt
import requests

from django.http import JsonResponse

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope


def items(request):
    '''
    List all item snippets
    '''
    if(request.method == 'GET'):
        # get all the items
        items = Item.objects.all()
        # serialize the item data
        serializer = ItemSerializer(items, context={'request': request}, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ItemSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

def item_detail(request, pk):
    try:
        # obtain the item with the passed id.
        item = Item.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = ItemSerializer(item, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the item
        item.delete()
        # return a no content response.
        return HttpResponse(status=204)
    elif(request.method == 'GET'):
        serializer = ItemSerializer(item)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)

def restaurants(request):
    '''
    List all restaurant snippets
    '''
    if(request.method == 'GET'):
        # get all the restaurants
        restaurants = Restaurant.objects.all()
        # serialize the restaurant data
        serializer = RestaurantSerializer(restaurants, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = RestaurantSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

def restaurant_detail(request, pk):
    try:
        # obtain the restaurant with the passed id.
        restaurant = Restaurant.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = RestaurantSerializer(restaurant, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the restaurant
        restaurant.delete()
        # return a no content response.
        return HttpResponse(status=204)
    elif(request.method == 'GET'):
        serializer = RestaurantSerializer(restaurant)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)


def order_detail(request, pk):


    try:
        # obtain the order with the passed id.
        order = Order.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the order
        order.delete()
        # return a no content response.
        return HttpResponse(status=204)
    elif(request.method == 'GET'):
        serializer = OrderSerializer(order)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def orders(request):
    headers = {
            "accept": "application/json",
            "x-client-id": "29201469c851556619451b35f5410292",
            "x-client-secret": "a55c7a6facea3ef186433d971e1754104d7ae474",
            "x-api-version": "2022-09-01",
            "content-type": "application/json"
        }
    url = "https://sandbox.cashfree.com/pg/orders"
    if(request.method == 'GET'):
        # get all the orders
        orders = Order.objects.all()
        # serialize the order data
        serializer = OrderSerializer(orders, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = OrderSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            payload = {
                "customer_details": {
                    "customer_id": data["nickname"],
                    "customer_email": data["user"],
                    "customer_phone": "7026521395"
                },
                "order_id": str(serializer.data["id"]),
                "order_amount": data["price"],
                "order_currency": "INR",
                "order_meta": {"return_url": "http://localhost:5173/checkout/complete/{order_id}"},
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
            # provide a Json Response with the data that was saved
            return JsonResponse(response.json(), status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)




@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})

    # auth0authorization/views.py

@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})

# auth0authorization/views.py


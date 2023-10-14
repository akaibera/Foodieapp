from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .serializers import *


@api_view(['GET'])
def VegHotels(request):
    veg_obj = VegHotel.objects.all()
    serializer = VegHotelSerializer(veg_obj,many=True)
    return Response({'status': 200,'playload': serializer.data})


# Retrieve a single VegHotel
@api_view(['GET'])
def veg_hotel_detail(request, pk):
    try:
        veg_hotel = VegHotel.objects.get(pk=pk)
        serializer = VegHotelSerializer(veg_hotel)
        return Response({'status': 200, 'Payload': serializer.data})
    except VegHotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegHotel not found'})

# Create a new VegHotel
@api_view(['POST'])
def veg_hotel_create(request):
    serializer = VegHotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})

# Update a VegHotel
@api_view(['PUT'])
def veg_hotel_update(request, pk):
    try:
        veg_hotel = VegHotel.objects.get(pk=pk)
        serializer = VegHotelSerializer(veg_hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except VegHotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegHotel not found'})

# Delete a VegHotel
@api_view(['DELETE'])
def veg_hotel_delete(request, pk):
    try:
        veg_hotel = VegHotel.objects.get(pk=pk)
        veg_hotel.delete()
        return Response({'status': 204, 'Payload': 'VegHotel deleted'})
    except VegHotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegHotel not found'})



#Itemlist Viewset

@api_view(['GET'])
def VegFoodItemList(request):
    veg_hotels = VegHotel.objects.all()
    data = []

    for veg_hotel in veg_hotels:
        veg_items = VegFoodItems.objects.filter(Hotel_name=veg_hotel)  # Correct the field name
        item_data = VegFoodItemSerializer(veg_items, many=True).data
        hotel_data = {
            # 'id': veg_hotel.Hotel_id,
            'Hotel_name': veg_hotel.Hotel_name,
            'Item_list': item_data
        }
        data.append(hotel_data)

    return Response({'status': 200, 'Payload': data})


# Create a new VegFoodItem
@api_view(['POST'])
def veg_food_item_create(request):
    serializer = VegFoodItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})

# Retrieve a single VegFoodItem
@api_view(['GET'])
def veg_food_item_detail(request, pk):
    try:
        veg_food_item = VegFoodItems.objects.get(pk=pk)
        serializer = VegFoodItemSerializer(veg_food_item)
        return Response({'status': 200, 'Payload': serializer.data})
    except VegFoodItems.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegFoodItem not found'})

# Update a VegFoodItem
@api_view(['PUT'])
def veg_food_item_update(request, pk):
    try:
        veg_food_item = VegFoodItems.objects.get(pk=pk)
        serializer = VegFoodItemSerializer(veg_food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except VegFoodItems.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegFoodItem not found'})

# Delete a VegFoodItem
@api_view(['DELETE'])
def veg_food_item_delete(request, pk):
    try:
        veg_food_item = VegFoodItems.objects.get(pk=pk)
        veg_food_item.delete()
        return Response({'status': 204, 'Payload': 'VegFoodItem deleted'})
    except VegFoodItems.DoesNotExist:
        return Response({'status': 404, 'Payload': 'VegFoodItem not found'})




#NonVeg  list Views

@api_view(['GET'])
def NonVegHotels(request):
    non_veg_obj = NonVegHotel.objects.all()
    serializer = NonVegHotelSerializer(non_veg_obj,many=True)
    return Response({'status': 200,'playload': serializer.data})



# Retrieve a single NONVegHotel
@api_view(['GET'])
def NonVeg_hotel_detail(request, pk):
    try:
        non_veg_hotel = NonVegHotel.objects.get(pk=pk)
        serializer = NonVegHotelSerializer(non_veg_hotel)
        return Response({'status': 200, 'Payload': serializer.data})
    except non_veg_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegHotel not found'})
    

# Create a new NONVegHotel
@api_view(['POST'])
def NonVeg_hotel_create(request):
    serializer = NonVegHotelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})


# Update a NONVegHotel
@api_view(['PUT'])
def NonVeg_hotel_update(request, pk):
    try:
        non_veg_hotel = NonVegHotel.objects.get(pk=pk)
        serializer = NonVegHotelSerializer(non_veg_hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except non_veg_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegHotel not found'})


# Delete a NonVegHotel
@api_view(['DELETE'])
def NonVeg_hotel_delete(request, pk):
    try:
        non_veg_hotel = NonVegHotel.objects.get(pk=pk)
        non_veg_hotel.delete()
        return Response({'status': 204, 'Payload': 'NonVegHotel deleted'})
    except non_veg_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegHotel not found'})

#Item list view
@api_view(['GET'])
def NonVegFoodItemList(request):
    non_veg_hotels = NonVegHotel.objects.all()
    data = []

    for non_veg_hotel in non_veg_hotels:
        non_veg_items = NonVegFoodItems.objects.filter(Nonveg_Hotel_name=non_veg_hotel)  # Correct the field name
        item_data = NonVegFoodItemSerializer(non_veg_items, many=True).data
        hotel_data = {
            # 'id': veg_hotel.Hotel_id,
            'Nonveg_Hotel_name': non_veg_hotel.Nonveg_Hotel_name,
            'Item_list': item_data
        }
        data.append(hotel_data)

    return Response({'status': 200, 'Payload': data})



# Create a new NonVegFoodItem
@api_view(['POST'])
def non_veg_food_item_create(request):
    serializer = NonVegFoodItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})

# Retrieve a single NOnVegFoodItem
@api_view(['GET'])
def non_veg_food_item_detail(request, pk):
    try:
        non_veg_food_item = VegFoodItems.objects.get(pk=pk)
        serializer = NonVegFoodItemSerializer(non_veg_food_item)
        return Response({'status': 200, 'Payload': serializer.data})
    except non_veg_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegFoodItem not found'})

# Update a VegFoodItem
@api_view(['PUT'])
def non_veg_food_item_update(request, pk):
    try:
        non_veg_food_item = NonVegFoodItems.objects.get(pk=pk)
        serializer = NonVegFoodItemSerializer(non_veg_food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except non_veg_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegFoodItem not found'})


# Delete a NonVegFoodItem
@api_view(['DELETE'])
def non_veg_food_item_delete(request, pk):
    try:
        non_veg_food_item = NonVegFoodItems.objects.get(pk=pk)
        non_veg_food_item.delete()
        return Response({'status': 204, 'Payload': 'NonVegFoodItem deleted'})
    except non_veg_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'NonVegFoodItem not found'})



#Chats List View

@api_view(['GET'])
def ChatsHotel(request):
    chat_obj = Chats.objects.all()
    serializer = ChatsSerializer(chat_obj,many=True)
    return Response({'status': 200,'playload': serializer.data})



# Retrieve a single ChatHotel
@api_view(['GET'])
def chats_hotel_detail(request, pk):
    try:
        chat_hotel = Chats.objects.get(pk=pk)
        serializer = ChatsSerializer(chat_hotel)
        return Response({'status': 200, 'Payload': serializer.data})
    except chat_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'ChatHotel not found'})
    

# Create a new  ChatHotel
@api_view(['POST'])
def chats_hotel_create(request):
    serializer = ChatsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})


# Update a ChatHotel
@api_view(['PUT'])
def chats_hotel_update(request, pk):
    try:
        chat_hotel = Chats.objects.get(pk=pk)
        serializer = ChatsSerializer(chat_hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except chat_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'Chats not found'})


# Delete a Chatotel
@api_view(['DELETE'])
def chat_hotel_delete(request, pk):
    try:
        chat_hotel = Chats.objects.get(pk=pk)
        chat_hotel.delete()
        return Response({'status': 204, 'Payload': 'Chats deleted'})
    except chat_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'Chats not found'})


#Item list view
@api_view(['GET'])
def chatFoodItemList(request):
    chat_hotels = Chats.objects.all()
    data = []

    for chat_hotel in chat_hotels:
        chat_items =ChatsItem.objects.filter(Chat_Hotel_name=chat_hotel)  # Correct the field name
        item_data = ChatsItemsSerializer(chat_items, many=True).data
        hotel_data = {
            # 'id': veg_hotel.Hotel_id,
            'Chat_Hotel_name': chat_hotel.Chat_Hotel_name,
            'Item_list': item_data
        }
        data.append(hotel_data)

    return Response({'status': 200, 'Payload': data})



# Create a new chatfood item
@api_view(['POST'])
def chat_food_item_create(request):
    serializer = ChatsItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})

# Retrieve a single ChatFoodItem
@api_view(['GET'])
def chat_food_item_detail(request, pk):
    try:
        chat_food_item = Chats.objects.get(pk=pk)
        serializer = ChatsItemsSerializer(chat_food_item)
        return Response({'status': 200, 'Payload': serializer.data})
    except chat_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'ChatFoodItem not found'})

# Update a ChatFoodItem
@api_view(['PUT'])
def chat_food_item_update(request, pk):
    try:
        chat_food_item = Chats.objects.get(pk=pk)
        serializer = ChatsItemsSerializer(chat_food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except chat_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'ChatFoodItem not found'})


# Delete a ChatFoodItem
@api_view(['DELETE'])
def chat_food_item_delete(request, pk):
    try:
        chat_food_item =Chats.objects.get(pk=pk)
        chat_food_item.delete()
        return Response({'status': 204, 'Payload': 'chatFoodItem deleted'})
    except chat_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'chatFoodItem not found'})




#Sweet List View

@api_view(['GET'])
def SweetHotelList(request):
    sweet_obj = Sweets.objects.all()
    serializer = SweetsSerializer(sweet_obj,many=True)
    return Response({'status': 200,'playload': serializer.data})



# Retrieve a single SweetsHotel
@api_view(['GET'])
def sweet_hotel_detail(request, pk):
    try:
        chat_hotel = Sweets.objects.get(pk=pk)
        serializer = SweetsSerializer(chat_hotel)
        return Response({'status': 200, 'Payload': serializer.data})
    except chat_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'SweetsHotel not found'})
    

# Create a new  SweetsHotel
@api_view(['POST'])
def sweet_hotel_create(request):
    serializer = SweetsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})


# Update a SweetsHotel
@api_view(['PUT'])
def sweet_hotel_update(request, pk):
    try:
        sweet_hotel = Sweets.objects.get(pk=pk)
        serializer = SweetsSerializer(sweet_hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except sweet_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'Sweets not found'})


# Delete Sweets Hotel
@api_view(['DELETE'])
def sweet_hotel_delete(request, pk):
    try:
        sweet_hotel = Sweets.objects.get(pk=pk)
        sweet_hotel.delete()
        return Response({'status': 204, 'Payload': 'Sweets deleted'})
    except sweet_hotel.DoesNotExist:
        return Response({'status': 404, 'Payload': 'Sweets not found'})


#Item list view
@api_view(['GET'])
def SweetFoodItemList(request):
    sweet_hotels = Sweets.objects.all()
    data = []

    for sweet_hotel in sweet_hotels:
        sweets_items = SweetsItem.objects.filter(Sweets_Hotel_name=sweet_hotel) # Correct the field name
        item_data = SweetsItemsSerializer(sweets_items, many=True).data
        hotel_data = {
            # 'id': veg_hotel.Hotel_id,
            'Sweets_Hotel_name': sweet_hotel.Sweets_Hotel_name,
            'Item_list': item_data
        }
        data.append(hotel_data)

    return Response({'status': 200, 'Payload': data})



# Create a new sweetfood item
@api_view(['POST'])
def sweet_food_item_create(request):
    serializer = SweetsItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201, 'Payload': serializer.data})
    return Response({'status': 400, 'Payload': serializer.errors})

# Retrieve a single SweetFoodItem
@api_view(['GET'])
def sweet_food_item_detail(request, pk):
    try:
        sweet_food_item = ChatsItem.objects.get(pk=pk)
        serializer = SweetsItemsSerializer(sweet_food_item)
        return Response({'status': 200, 'Payload': serializer.data})
    except VegFoodItems.DoesNotExist:
        return Response({'status': 404, 'Payload': 'SweetFoodItem not found'})

# Update a SweetFoodItem
@api_view(['PUT'])
def sweet_food_item_update(request, pk):
    try:
        sweet_food_item = ChatsItem.objects.get(pk=pk)
        serializer = ChatsItemsSerializer(sweet_food_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'Payload': serializer.data})
        return Response({'status': 400, 'Payload': serializer.errors})
    except sweet_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'SweetFoodItem not found'})


# Delete a ChatFoodItem
@api_view(['DELETE'])
def sweet_food_item_delete(request, pk):
    try:
        sweet_food_item =ChatsItem.objects.get(pk=pk)
        sweet_food_item.delete()
        return Response({'status': 204, 'Payload': 'SweetFoodItem deleted'})
    except sweet_food_item.DoesNotExist:
        return Response({'status': 404, 'Payload': 'SweetFoodItem not found'})
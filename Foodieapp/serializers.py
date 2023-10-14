from rest_framework import serializers
from .models import *


class VegHotelSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = VegHotel
        fields = '__all__'

class VegFoodItemSerializer(serializers.ModelSerializer):
    # Hotel_name = serializers.CharField(source='Hotel_name.Hotel_name')
    # vegfooditems_set = VegHotelSerializer(many=True, read_only=True)

    class Meta:
        model = VegFoodItems
        fields = '__all__'


class NonVegHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonVegHotel  # Specify the model that the serializer is associated with
        fields = '__all__'  # You can also specify the fields you want to include in the serializer


class NonVegFoodItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = NonVegFoodItems
        fields = '__all__'


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats  # Specify the model here
        fields = '__all__'  # You can specify the fields you want to include

    # You can also add additional configuration options here

class ChatsItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatsItem
        fields = '__all__'


class SweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweets  # Specify the model here
        fields = '__all__'  # You can specify the fields you want to include

    # You can also add additional configuration options here

class SweetsItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SweetsItem
        fields = '__all__'



from django.urls import path

from Foodieapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('veg-hotels/',views.VegHotels),
    # Retrieve a single VegHotel, update, and delete a VegHotel
    path('veg-hotels/<int:pk>/', views.veg_hotel_detail, name='veg-hotel-detail'),

    # Create a new VegHotel
    path('veg-hotels/create/', views.veg_hotel_create, name='veg-hotel-create'),

    # Update a VegHotel
    path('veg-hotels/update/<int:pk>/', views.veg_hotel_update, name='veg-hotel-update'),

    # Delete a VegHotel
    path('veg-hotels/delete/<int:pk>/', views.veg_hotel_delete, name='veg-hotel-delete'),

    #List Out all Items
    path('food-items/',views.VegFoodItemList),

    # Retrieve, update, and delete a single VegFoodItem
    path('veg-food-items/<int:pk>/', views.veg_food_item_detail, name='veg-food-item-detail'),

    # Create a new VegFoodItem
    path('veg-food-items/create/', views.veg_food_item_create, name='veg-food-item-create'),

    # Update a VegFoodItem
    path('veg-food-items/update/<int:pk>/', views.veg_food_item_update, name='veg-food-item-update'),

    # Delete a VegFoodItem
    path('veg-food-items/delete/<int:pk>/', views.veg_food_item_delete, name='veg-food-item-delete'),


    #NON HOtel Lists VEG URLS
    path('non-veg-hotels/', views.NonVegHotels, name='non_veg_hotels'),
    path('non-veg-hotel-detail/<int:pk>/', views.NonVeg_hotel_detail, name='non_veg_hotel_detail'),
    path('non-veg-hotel-create/', views.NonVeg_hotel_create, name='non_veg_hotel_create'),
    path('non-veg-hotel-update/<int:pk>/', views.NonVeg_hotel_update, name='non_veg_hotel_update'),
    path('non-veg-hotel-delete/<int:pk>/', views.NonVeg_hotel_delete, name='non_veg_hotel_delete'),
    #NonVeg Item List Urls
    path('non-veg-food-items/', views.NonVegFoodItemList, name='non_veg_food_items'),
    path('non-veg-food-item-create/', views.non_veg_food_item_create, name='non_veg_food_item_create'),
    path('non-veg-food-item-detail/<int:pk>/', views.non_veg_food_item_detail, name='non_veg_food_item_detail'),
    path('non-veg-food-item-update/<int:pk>/', views.non_veg_food_item_update, name='non_veg_food_item_update'),
    path('non-veg-food-item-delete/<int:pk>/', views.non_veg_food_item_delete, name='non_veg_food_item_delete'),

    #Chat's Hotel List Urls
    path('chats-hotels/', views.ChatsHotel, name='chats_hotels'),
    path('chats-hotel-detail/<int:pk>/', views.chats_hotel_detail, name='chats_hotel_detail'),
    path('chats-hotel-create/', views.chats_hotel_create, name='chats_hotel_create'),
    path('chats-hotel-update/<int:pk>/', views.chats_hotel_update, name='chats_hotel_update'),
    path('chat-hotel-delete/<int:pk>/', views.chat_hotel_delete, name='chat_hotel_delete'),

    #Chat Item List Item
    path('chat-food-items/', views.chatFoodItemList, name='chat_food_items'),
    path('chat-food-item-create/', views.chat_food_item_create, name='chat_food_item_create'),
    path('chat-food-item-detail/<int:pk>/', views.chat_food_item_detail, name='chat_food_item_detail'),
    path('chat-food-item-update/<int:pk>/', views.chat_food_item_update, name='chat_food_item_update'),
    path('chat-food-item-delete/<int:pk>/', views.chat_food_item_delete, name='chat_food_item_delete'),

    # Sweet Hotel Lists
    path('sweets-hotels/', views.SweetHotelList, name='sweets_hotels'),
    path('sweets-hotel-detail/<int:pk>/', views.sweet_hotel_detail, name='sweets_hotel_detail'),
    path('sweets-hotel-create/', views.sweet_hotel_create, name='sweets_hotel_create'),
    path('sweets-hotel-update/<int:pk>/', views.sweet_hotel_update, name='sweets_hotel_update'),
    path('sweets-hotel-delete/<int:pk>/', views.sweet_hotel_delete, name='sweets_hotel_delete'),

    #Sweet Item Lists
    path('sweet-food-items/', views.SweetFoodItemList, name='sweet_food_items_list'),
    path('sweet-food-item-create/', views.sweet_food_item_create, name='sweet_food_item_create'),
    path('sweet-food-item-detail/<int:pk>/', views.sweet_food_item_detail, name='sweet_food_item_detail'),
    path('sweet-food-item-update/<int:pk>/', views.sweet_food_item_update, name='sweet_food_item_update'),
    path('sweet-food-item-delete/<int:pk>/', views.sweet_food_item_delete, name='sweet_food_item_delete'),
    
]








if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
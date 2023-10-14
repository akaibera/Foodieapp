from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Foodie"
admin.site.site_title = "Foodie"
admin.site.index_title = "Order Food and Grociries at your door step"

admin.site.register(VegHotel)
admin.site.register(VegFoodItems)
admin.site.register(NonVegHotel)
admin.site.register(NonVegFoodItems)
admin.site.register(Chats)
admin.site.register(ChatsItem)
admin.site.register(Sweets)
admin.site.register(SweetsItem)
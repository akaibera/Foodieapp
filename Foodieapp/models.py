from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.



class VegHotel(models.Model):
    Hotel_name = models.CharField(max_length=250,unique=True)
    Hotel_id = models.AutoField(primary_key=True)
    Hotel_image = models.ImageField(max_length=250,upload_to='images/')
    Hotel_Address = models.CharField(max_length=255)

    def __str__(self):
        return self.Hotel_name
    
class VegFoodItems(models.Model):
    Hotel_name= models.ForeignKey(VegHotel, on_delete=models.CASCADE, related_name='hotel_Name')
    Item_name = models.CharField(max_length=250)
    Item_image =  models.ImageField(max_length=250,default=None,null=True,blank=True,upload_to='images/')
    Item_price = models.FloatField(default=0.0,     
        blank=True,        
        null=True,         
        help_text="Price in INR",  
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]  
    )
    item_quantity = models.PositiveIntegerField(
        default=0,  
        validators=[MinValueValidator(1), MaxValueValidator(100)]  
    )

    def __str__(self):
        return self.Item_name
    

class NonVegHotel(models.Model):
    Nonveg_Hotel_name = models.CharField(max_length=250,unique=True)
    Nonveg_Hotel_id = models.AutoField(primary_key=True)
    Hotel_image = models.ImageField(max_length=250,upload_to='images/')
    Hotel_Address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.Nonveg_Hotel_name

class NonVegFoodItems(models.Model):
    Nonveg_Hotel_name= models.ForeignKey(NonVegHotel, on_delete=models.CASCADE, related_name='non_hotel_Name')
    Item_name = models.CharField(max_length=250)
    Item_image =  models.ImageField(max_length=250,default=None,null=True,blank=True,upload_to='images/')
    Item_price = models.FloatField(default=0.0,     
        blank=True,        
        null=True,         
        help_text="Price in INR",  
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]  
    )
    item_quantity = models.PositiveIntegerField(
        default=0,  
        validators=[MinValueValidator(1), MaxValueValidator(100)]  
    )

    def __str__(self):
        return self.Item_name
    

class Chats(models.Model):
    Chat_Hotel_name = models.CharField(max_length=250,unique=True)
    Chats_Hotel_id = models.AutoField(primary_key=True)
    Hotel_image = models.ImageField(max_length=250,upload_to='images/')
    Hotel_Address = models.CharField(max_length=255)

    def __str__(self):
        return self.Chat_Hotel_name
    
class ChatsItem(models.Model):
    Chat_Hotel_name= models.ForeignKey(Chats, on_delete=models.CASCADE, related_name='chats_hotel_Name')
    Item_name = models.CharField(max_length=250)
    Item_image =  models.ImageField(max_length=250,default=None,null=True,blank=True,upload_to='images/')
    Item_price = models.FloatField(default=0.0,     
        blank=True,        
        null=True,         
        help_text="Price in INR",  
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]  
    )
    item_quantity = models.PositiveIntegerField(
        default=0,  
        validators=[MinValueValidator(1), MaxValueValidator(100)]  
    )

    def __str__(self):
        return self.Item_name


class Sweets(models.Model):
    Sweets_Hotel_name = models.CharField(max_length=250,unique=True)
    Sweets_Hotel_id = models.AutoField(primary_key=True)
    Hotel_image = models.ImageField(max_length=250,upload_to='images/')
    Hotel_Address = models.CharField(max_length=255)

    def __str__(self):
        return self.Sweets_Hotel_name
    

class SweetsItem(models.Model):
    Sweets_Hotel_name= models.ForeignKey(Sweets, on_delete=models.CASCADE, related_name='sweets_hotel_Name')
    Item_name = models.CharField(max_length=250)
    Item_image =  models.ImageField(max_length=250,default=None,null=True,blank=True,upload_to='images/')
    Item_price = models.FloatField(default=0.0,     
        blank=True,        
        null=True,         
        help_text="Price in INR",  
        validators=[MinValueValidator(0.0), MaxValueValidator(1000.0)]  
    )
    item_quantity = models.PositiveIntegerField(
        default=0,  
        validators=[MinValueValidator(1), MaxValueValidator(100)]  
    )

    def __str__(self):
        return self.Item_name




    


    

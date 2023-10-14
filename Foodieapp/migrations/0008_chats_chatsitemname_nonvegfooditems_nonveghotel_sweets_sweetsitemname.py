# Generated by Django 3.1 on 2023-10-13 14:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodieapp', '0007_auto_20231013_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('Chat_Hotel_name', models.CharField(max_length=250, unique=True)),
                ('Hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hotel_image', models.ImageField(max_length=250, upload_to='images/')),
                ('Hotel_Address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NonVegHotel',
            fields=[
                ('Nonveg_Hotel_name', models.CharField(max_length=250, unique=True)),
                ('Hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hotel_image', models.ImageField(max_length=250, upload_to='images/')),
                ('Hotel_Address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('Sweets_Hotel_name', models.CharField(max_length=250, unique=True)),
                ('Hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hotel_image', models.ImageField(max_length=250, upload_to='images/')),
                ('Hotel_Address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SweetsItemName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=250)),
                ('Item_image', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='images/')),
                ('Item_price', models.FloatField(blank=True, default=0.0, help_text='Price in INR', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('item_quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Sweets_Hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_Name', to='Foodieapp.sweets')),
            ],
        ),
        migrations.CreateModel(
            name='NonVegFoodItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=250)),
                ('Item_image', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='images/')),
                ('Item_price', models.FloatField(blank=True, default=0.0, help_text='Price in INR', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('item_quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Nonveg_Hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='non_hotel_Name', to='Foodieapp.nonveghotel')),
            ],
        ),
        migrations.CreateModel(
            name='ChatsItemName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=250)),
                ('Item_image', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='images/')),
                ('Item_price', models.FloatField(blank=True, default=0.0, help_text='Price in INR', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('item_quantity', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Chat_Hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_hotel_Name', to='Foodieapp.chats')),
            ],
        ),
    ]
# Generated by Django 3.1 on 2023-10-13 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodieapp', '0011_auto_20231013_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsitem',
            name='Chat_Hotel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_hotel_Name', to='Foodieapp.chats'),
        ),
    ]

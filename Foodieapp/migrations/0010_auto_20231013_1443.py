# Generated by Django 3.1 on 2023-10-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodieapp', '0009_auto_20231013_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sweetsitemname',
            name='Sweets_Hotel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sweets_hotel_Name', to='Foodieapp.sweets'),
        ),
    ]
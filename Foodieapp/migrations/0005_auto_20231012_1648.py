# Generated by Django 3.1 on 2023-10-12 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foodieapp', '0004_auto_20231012_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegfooditems',
            name='hotel_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_Name', to='Foodieapp.veghotel'),
        ),
    ]

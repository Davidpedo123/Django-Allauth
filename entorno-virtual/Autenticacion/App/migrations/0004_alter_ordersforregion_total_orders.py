# Generated by Django 5.0.1 on 2024-02-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_ordersforregion_alter_productsdescuento_discontinued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersforregion',
            name='total_orders',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_ordersforregion_total_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('gender', models.CharField(max_length=100)),
                ('License', models.CharField(max_length=100)),
            ],
        ),
    ]
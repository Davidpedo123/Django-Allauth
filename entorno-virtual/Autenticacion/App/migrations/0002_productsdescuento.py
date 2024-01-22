# Generated by Django 4.2.5 on 2024-01-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsDescuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Discontinued', models.DecimalField(decimal_places=3, max_digits=10)),
                ('imagen', models.CharField(max_length=40000)),
            ],
        ),
    ]
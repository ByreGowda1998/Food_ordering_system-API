# Generated by Django 4.1.4 on 2023-01-20 07:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0006_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('total_order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

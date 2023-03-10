# Generated by Django 4.1.4 on 2023-01-19 12:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food_order', '0002_alter_cartitem_food_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=100)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_id', to='food_order.cart')),
                ('cupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupon', to='food_order.coupon')),
            ],
        ),
    ]

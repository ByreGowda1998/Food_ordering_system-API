# Generated by Django 4.1.4 on 2023-01-18 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_display', '0010_alter_food_food_type'),
        ('food_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='food_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_item', to='food_display.food'),
        ),
    ]

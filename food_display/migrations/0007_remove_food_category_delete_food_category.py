# Generated by Django 4.1.4 on 2023-01-16 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_display', '0006_food_category_food_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.DeleteModel(
            name='Food_Category',
        ),
    ]

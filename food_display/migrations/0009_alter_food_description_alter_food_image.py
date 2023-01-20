# Generated by Django 4.1.4 on 2023-01-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_display', '0008_food_category_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='media/default.jpeg', upload_to='media/'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-06 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_display', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='Price',
            new_name='price',
        ),
    ]

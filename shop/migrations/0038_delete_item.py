# Generated by Django 4.1.3 on 2023-01-08 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_remove_list_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
# Generated by Django 4.1.3 on 2023-01-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_alter_item_name_remove_list_item_list_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

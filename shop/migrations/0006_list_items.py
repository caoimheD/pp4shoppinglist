# Generated by Django 4.1.3 on 2022-12-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_item_remove_list_item_done_remove_list_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='items',
            field=models.ManyToManyField(to='shop.item'),
        ),
    ]
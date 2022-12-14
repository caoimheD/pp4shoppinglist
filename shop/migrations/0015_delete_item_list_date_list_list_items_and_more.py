# Generated by Django 4.1.3 on 2022-12-23 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_item_eachitem_remove_list_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='list',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='list_items',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

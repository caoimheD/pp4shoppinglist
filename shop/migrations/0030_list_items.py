# Generated by Django 4.1.3 on 2023-01-05 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_remove_list_item_alter_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.item'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_delete_item_remove_list_excerpt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default=True, max_length=50)),
                ('item_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='item_done',
        ),
        migrations.RemoveField(
            model_name='list',
            name='item_name',
        ),
    ]

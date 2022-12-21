# Generated by Django 4.1.3 on 2022-12-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_list_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='list',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='list',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]

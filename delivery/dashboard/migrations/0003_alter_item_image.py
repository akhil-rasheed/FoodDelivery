# Generated by Django 4.1.5 on 2023-01-07 05:51

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230106_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=dashboard.models.upload_to),
        ),
    ]
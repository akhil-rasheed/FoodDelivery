# Generated by Django 2.2.28 on 2023-01-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230109_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.EmailField(default='akhilrasheed16@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]

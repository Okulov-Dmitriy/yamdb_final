# Generated by Django 3.0 on 2021-08-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('reviews', '0006_auto_20210820_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=None, null=True),
        ),
    ]

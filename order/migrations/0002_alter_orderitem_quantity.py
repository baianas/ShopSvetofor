# Generated by Django 3.2 on 2021-12-24 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
    ]

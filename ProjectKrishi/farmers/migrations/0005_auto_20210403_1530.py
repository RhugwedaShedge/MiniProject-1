# Generated by Django 3.1.7 on 2021-04-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0004_auto_20210403_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipments',
            name='min_purchase',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=100),
        ),
        migrations.AddField(
            model_name='goods',
            name='min_purchase',
            field=models.DecimalField(decimal_places=0, default=5, max_digits=100),
        ),
    ]

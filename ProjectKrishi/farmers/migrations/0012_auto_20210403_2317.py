# Generated by Django 3.1.4 on 2021-04-03 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0011_cartitem_customer_customercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farmers.customercart'),
        ),
    ]

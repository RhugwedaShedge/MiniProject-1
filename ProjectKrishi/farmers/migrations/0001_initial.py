# Generated by Django 3.1.4 on 2021-03-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='product_default.png', null=True, upload_to='')),
                ('product_name', models.CharField(max_length=120, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=100)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
    ]
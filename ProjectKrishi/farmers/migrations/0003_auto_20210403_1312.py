# Generated by Django 3.1.7 on 2021-04-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_auto_20210329_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('stock', models.DecimalField(decimal_places=0, max_digits=100)),
                ('desc', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='Description',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, default='product_default.png', null=True, upload_to=''),
        ),
    ]

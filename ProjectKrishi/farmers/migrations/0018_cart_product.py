
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0017_delete_cart'),
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
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]

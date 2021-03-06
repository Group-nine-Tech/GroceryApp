# Generated by Django 3.1.1 on 2020-09-17 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoolerBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_number', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('unlock_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('transport_mode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_time', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.delivery')),
                ('shipping_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shippingprovider')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-09 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transport', '0002_vehicle_vehicle_live'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startpoint', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=200)),
                ('booked_date', models.DateTimeField()),
                ('booking_status', models.CharField(default='pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=250)),
                ('driver_phone', models.IntegerField()),
                ('driver_address', models.CharField(max_length=400)),
                ('driver_age', models.IntegerField()),
                ('vehicle_type', models.CharField(max_length=200)),
                ('vehicle_reg_num', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='My_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user_name', models.CharField(max_length=250)),
                ('user_phone', models.IntegerField()),
                ('user_addr', models.CharField(max_length=250)),
                ('user_email', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.AlterField(
            model_name='vehicle_live',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.driver'),
        ),
        migrations.DeleteModel(
            name='vehicle',
        ),
        migrations.AddField(
            model_name='bookings',
            name='booked_driver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Transport.driver'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transport.My_user'),
        ),
    ]

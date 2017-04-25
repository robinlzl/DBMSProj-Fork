# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('abb_state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Detail',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Room',
            fields=[
                ('room_no', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Hotel_Detail')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('departure_city', models.CharField(max_length=20)),
                ('arrival_city', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=10)),
                ('ticket_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Train_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.User_Detail')),
            ],
        ),
        migrations.CreateModel(
            name='Train_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_city', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('arrival_time', models.DateTimeField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Train')),
            ],
        ),
        migrations.CreateModel(
            name='Train_Sub_Order',
            fields=[
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
                ('arrival_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_train_schedule', to='webapp.Train_Schedule')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_train_schedule', to='webapp.Train_Schedule')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Train')),
            ],
        ),
        migrations.AddField(
            model_name='hotel_order',
            name='hotel_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Hotel_Room'),
        ),
        migrations.AddField(
            model_name='hotel_order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='hotel_room',
            unique_together=set([('room_no', 'hotel')]),
        ),
    ]
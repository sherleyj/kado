# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 20:47
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WishListApp', '0006_auto_20160316_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistitem',
            old_name='descripton',
            new_name='product_description',
        ),
        migrations.AddField(
            model_name='kadouser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 9, 19, 35, 45, 964840, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 9, 20, 47, 29, 311842, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='quantity',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='store_shortcut_icon',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='wishlistitem',
            name='user_comment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
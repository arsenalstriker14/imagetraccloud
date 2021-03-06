# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 09:04
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_date', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('mfg', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('vendor_number', models.CharField(blank=True, max_length=30, null=True)),
                ('order_date', models.CharField(blank=True, max_length=30, null=True)),
                ('received_dc', models.CharField(blank=True, max_length=30, null=True)),
                ('received_137', models.CharField(blank=True, max_length=30, null=True)),
                ('received_buyer', models.CharField(blank=True, max_length=40, null=True)),
                ('received_other', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('photo_dldate', models.CharField(blank=True, max_length=50, null=True)),
                ('whowhen', models.CharField(blank=True, max_length=100, null=True)),
                ('studio_out', models.CharField(blank=True, max_length=30, null=True)),
                ('checked_out', models.CharField(blank=True, max_length=100, null=True)),
                ('have_image', models.CharField(blank=True, max_length=30, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('shooting_instructions', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('studio_in', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('short_sku', models.CharField(blank=True, max_length=30, null=True)),
                ('from_file', models.CharField(blank=True, max_length=30, null=True)),
                ('sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('first', models.CharField(blank=True, max_length=5, null=True)),
                ('first_date', models.CharField(blank=True, max_length=30, null=True)),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('merch_to_137', models.CharField(blank=True, max_length=200, null=True)),
                ('product_class', models.CharField(blank=True, max_length=4, null=True)),
                ('dc_received_u', models.IntegerField(blank=True, null=True)),
                ('curr_dc_oh_u', models.IntegerField(blank=True, null=True)),
                ('dc_curr_oo_u', models.IntegerField(blank=True, null=True)),
                ('na', models.CharField(blank=True, max_length=5, null=True)),
                ('size_type', models.CharField(blank=True, max_length=10, null=True)),
                ('color_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=3, null=True)),
                ('product_class', models.CharField(blank=True, max_length=4, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_ns', models.CharField(max_length=30)),
                ('brand', models.CharField(blank=True, max_length=20, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('ad_date', models.CharField(blank=True, max_length=20, null=True)),
                ('mfg', models.CharField(blank=True, max_length=30, null=True)),
                ('already_tracked', models.CharField(blank=True, default='None', max_length=300, null=True)),
                ('na', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ColorCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColorGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('hexcode', models.CharField(max_length=6, unique=True)),
                ('description', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Admin', 'Admin'), ('Advertising', 'Advertising'), ('Art', 'Art'), ('Layout', 'Layout'), ('Copy', 'Copy'), ('Purchasing', 'Purchasing'), ('IT', 'IT')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Deployed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('operator', models.CharField(blank=True, max_length=50, null=True)),
                ('filenames', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='FirstReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(blank=True, max_length=30, null=True)),
                ('dc_received_u', models.IntegerField(blank=True, null=True)),
                ('curr_dc_oh_u', models.IntegerField(blank=True, null=True)),
                ('dc_curr_oo_u', models.IntegerField(blank=True, null=True)),
                ('date_received', models.CharField(blank=True, max_length=20, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('short_sku', models.CharField(blank=True, max_length=30, null=True)),
                ('size_type', models.CharField(blank=True, max_length=10, null=True)),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('vendor_style', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('color_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('have_image', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_date', models.CharField(blank=True, max_length=50, null=True)),
                ('order_date', models.CharField(blank=True, max_length=50, null=True)),
                ('received_dc', models.CharField(blank=True, max_length=30, null=True)),
                ('received_137', models.CharField(blank=True, max_length=30, null=True)),
                ('from_file', models.CharField(blank=True, max_length=30, null=True)),
                ('photo_dldate', models.DateField(blank=True, null=True)),
                ('whowhen', models.CharField(blank=True, max_length=100, null=True)),
                ('studio_out', models.CharField(blank=True, max_length=50, null=True)),
                ('checked_out', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('studio_in', models.CharField(blank=True, max_length=50, null=True)),
                ('merch_to_137', models.CharField(blank=True, max_length=200, null=True)),
                ('product_class', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=30, unique=True)),
                ('ad_date', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('item_name', models.CharField(blank=True, max_length=210, null=True)),
                ('comments', models.TextField(blank=True, max_length=2000, null=True)),
                ('reply', models.TextField(blank=True, max_length=2000, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=7, null=True)),
                ('item_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.CharField(max_length=3)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LargeWebfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_sku', models.CharField(max_length=30)),
                ('filename', models.CharField(max_length=50)),
                ('mod_date', models.CharField(blank=True, max_length=200, null=True)),
                ('item_ns', models.CharField(max_length=30, null=True)),
                ('sku', models.CharField(max_length=30, null=True)),
                ('sku_ns', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MSWebfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_sku', models.CharField(max_length=30)),
                ('filename', models.CharField(max_length=50)),
                ('item_ns', models.CharField(max_length=30, null=True)),
                ('sku', models.CharField(max_length=30, null=True)),
                ('sku_ns', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OneImageFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PrintFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assoc_sku', models.CharField(max_length=30)),
                ('filename', models.CharField(blank=True, max_length=500, null=True)),
                ('path', models.CharField(blank=True, max_length=200, null=True)),
                ('mod_date', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(max_length=30)),
                ('filename', models.CharField(blank=True, max_length=50, null=True)),
                ('processor', models.CharField(blank=True, max_length=50, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('product_class', models.CharField(blank=True, max_length=10, null=True)),
                ('upload_date', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_date', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('item_no', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('mfg', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('vendor_number', models.CharField(blank=True, max_length=30, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('received_dc', models.DateField(blank=True, null=True)),
                ('received_137', models.CharField(blank=True, max_length=30, null=True)),
                ('received_buyer', models.CharField(blank=True, max_length=40, null=True)),
                ('received_other', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('photo_dldate', models.CharField(blank=True, max_length=50, null=True)),
                ('whowhen', models.CharField(blank=True, max_length=100, null=True)),
                ('studio_out', models.DateField(blank=True, null=True)),
                ('checked_out', models.CharField(blank=True, max_length=100, null=True)),
                ('have_image', models.CharField(blank=True, max_length=30, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('shooting_instructions', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('studio_in', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('short_sku', models.CharField(blank=True, max_length=30, null=True)),
                ('from_file', models.CharField(blank=True, max_length=30, null=True)),
                ('sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('first', models.CharField(blank=True, max_length=5, null=True)),
                ('first_date', models.CharField(blank=True, max_length=30, null=True)),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('merch_to_137', models.CharField(blank=True, max_length=200, null=True)),
                ('dc_received_u', models.IntegerField(blank=True, null=True)),
                ('curr_dc_oh_u', models.IntegerField(blank=True, null=True)),
                ('dc_curr_oo_u', models.IntegerField(blank=True, null=True)),
                ('na', models.CharField(blank=True, max_length=5, null=True)),
                ('size_type', models.CharField(blank=True, max_length=10, null=True)),
                ('color_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('product_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b5.Buyers', to_field='product_class')),
            ],
        ),
        migrations.CreateModel(
            name='RegularWebfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_sku', models.CharField(max_length=30)),
                ('filename', models.CharField(max_length=50)),
                ('item_ns', models.CharField(max_length=30, null=True)),
                ('sku', models.CharField(max_length=30, null=True)),
                ('sku_ns', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReplacedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('old_filename', models.CharField(blank=True, max_length=50, null=True)),
                ('new_filename', models.CharField(blank=True, max_length=50, null=True)),
                ('change_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RumbaProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('mfg', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('vendor_number', models.CharField(blank=True, max_length=30, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default='None', max_length=200, null=True)),
                ('item_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('short_sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku', models.CharField(blank=True, max_length=30, null=True)),
                ('sku_ns', models.CharField(blank=True, max_length=30, null=True)),
                ('product_class', models.CharField(blank=True, max_length=4, null=True)),
                ('merch_to_137', models.CharField(blank=True, max_length=200, null=True)),
                ('dc_received_u', models.IntegerField(blank=True, null=True)),
                ('curr_dc_oh_u', models.IntegerField(blank=True, null=True)),
                ('dc_curr_oo_u', models.IntegerField(blank=True, null=True)),
                ('size_type', models.CharField(blank=True, max_length=10, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color_desc', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThumbWebfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_sku', models.CharField(max_length=30)),
                ('filename', models.CharField(max_length=50)),
                ('item_ns', models.CharField(max_length=30, null=True)),
                ('sku', models.CharField(max_length=30, null=True)),
                ('sku_ns', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=64)),
                ('position', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('extension', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('notes', models.TextField(blank=True, max_length=2000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__last_name'],
            },
        ),
        migrations.CreateModel(
            name='WatchedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(blank=True, max_length=30, null=True)),
                ('desc', models.CharField(blank=True, max_length=210, null=True)),
                ('comments', models.TextField(blank=True, max_length=2000, null=True)),
                ('confirmed_placed', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('watched_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='b5.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='replacedimage',
            name='processor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='b5.UserProfile'),
        ),
        migrations.AddField(
            model_name='oneimagefiles',
            name='filenames',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b5.PrintFile'),
        ),
        migrations.AlterUniqueTogether(
            name='inventoryproduct',
            unique_together=set([('sku', 'source')]),
        ),
        migrations.AddField(
            model_name='department',
            name='member',
            field=models.ManyToManyField(to='b5.UserProfile'),
        ),
    ]

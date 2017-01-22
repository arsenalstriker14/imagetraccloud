#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by krc.nyc on 2009-05-15.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from django.contrib import admin
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import ChoicesFieldListFilter




class ProductInline(admin.TabularInline):
	model = Product
    # formset = # Yours


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns','desc', 'mfg', 'confirmed_placed', "buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", 'na')
    search_fields = ('ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns', 'first', 'buyer', 'desc', 'mfg')
    list_filter = ('ad_date',)
    list_editable = ('ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns','desc', 'mfg', 'confirmed_placed', "buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", 'na')
    formset = ProductFormSet
    # add_form_template = "templates/product_add_form.html"

class AdProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns','desc', 'mfg', 'confirmed_placed', "buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", 'na')
    search_fields = ('ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns', 'first', 'buyer', 'desc', 'mfg')
    list_filter = ('ad_date',)
    list_editable = ('ad_date', 'first_date', 'item_no', 'item_ns', 'sku', 'sku_ns','desc', 'mfg', 'confirmed_placed', "buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", 'na')
    formset = AdProductFormSet

class WatchedItemAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "watched_by":
            kwargs["queryset"] = WatchedItem.objects.filter(owner=request.user)
        return super(WatchedItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class HotItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'item_no', 'item_name', 'ad_date', 'comments', 'reply')
    search_fields = ('create_date', 'item_no', 'item_name', 'ad_date')
    list_filter = ('create_date', 'item_no', 'item_name', 'ad_date')
    list_editable = ('create_date', 'item_no', 'item_name', 'ad_date', 'comments', 'reply')
    formset = HIFormSet

class FRInline(admin.TabularInline):
    model = FirstReceipt


class FRAdmin(admin.ModelAdmin):
    list_display = ('id',  "buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", "date_received", "item_ns", "short_sku", "item_no", "vendor_style", "description", "have_image", "ad_date", "order_date", "received_dc", "received_137", "from_file", "photo_dldate", "whowhen", "studio_out", "checked_out", "confirmed_placed", "studio_in", "merch_to_137")
    search_fields = ('buyer', 'item_no', 'item_ns', 'short_sku', 'description')
    list_filter = ('buyer',)
    list_editable = ("buyer", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", "date_received", "item_ns", "short_sku", "item_no", "vendor_style", "description", "have_image", "ad_date", "order_date", "received_dc", "received_137", "from_file", "photo_dldate", "whowhen", "studio_out", "checked_out", "confirmed_placed", "studio_in", "merch_to_137")
    formset = FRFormSet


admin.site.register(ColorGrid)
admin.site.register(Product, ProductAdmin)
admin.site.register(FirstReceipt, FRAdmin)
admin.site.register(CheckProduct)
admin.site.register(UserProfile)
admin.site.register(ProcessedFiles)
admin.site.register(Buyers)
admin.site.register(Deployed)
admin.site.register(InventoryProduct)
admin.site.register(AdProduct, AdProductAdmin)
admin.site.register(ReplacedImage)
admin.site.register(WatchedItem, WatchedItemAdmin)
admin.site.register(HotItem, HotItemAdmin)

def main():
    pass


if __name__ == '__main__':
    main()


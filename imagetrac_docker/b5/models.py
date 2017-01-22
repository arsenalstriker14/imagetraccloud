from django.db import models
from django import forms
from django.core.files.storage import FileSystemStorage
from django.contrib.postgres.fields import JSONField
from django.forms import ModelForm
from django.db.models import TextField
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.files import File
from django.core.validators import RegexValidator
import django_filters
import datetime
from datetime import date

class WarningManager(models.Manager):
    def is_hot(self):
        ad = datetime.datetime.strptime(self.ad_date, "%m%d%y")
        today = datetime.date.today()

        threshold_time = ad - datetime.timedelta(days=32)
        threshold_time = threshold_time.date()

        if today > threshold_time:
            return u'%s %s %s %s %s' % (self.ad_date, ' ', self.item_no, ' ', self.desc)

GROUP_CHOICES = (
    ('Admin', 'Admin'),
    ('Advertising', 'Advertising'),
    ('Art', 'Art'),
    ('Layout', 'Layout'),
    ('Copy', 'Copy'),
    ('Purchasing', 'Purchasing'),
    ('IT', 'IT'),
)

class UserProfile(models.Model):  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, null=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=64, unique=False)
    position = models.CharField(max_length=64, unique=False, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=False, blank=True, null=True)
    extension = models.CharField(max_length=15, unique=False, blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=False, blank=True, null=True)
    fax = models.CharField(max_length=15, unique=False, blank=True, null=True)
    notes = models.TextField(max_length=2000, blank=True, null=True)
    email = models.EmailField()


    def __str__(self):
        return u'%s' % (self.fullname) 
        
    class Meta:
            ordering = ["user__last_name"]

    class Admin: 
        pass  

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
  
@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        UserProfile.objects.create(user=kwargs.get('instance'))

class Department(models.Model):
    name = models.CharField(max_length=64, choices=GROUP_CHOICES)
    member = models.ManyToManyField(UserProfile)

    def __str__(self):
        return u'%s' % self.name

    class Admin: 
        pass

class ColorGrid(models.Model):
    color = models.CharField(max_length=30, unique=False, blank=True, null=True)
    hexcode = models.CharField(max_length=6, unique=True, blank=False, null=False)
    description = models.CharField(max_length=300, unique=True, blank=False, null=False)

    def __str__(self):
        return u'%s %s %s' % (self.color, self.hexcode, self.description)

    class Admin: 
        pass

class ColorCode(models.Model):
    code = models.CharField(max_length=3, unique=True, blank=False, null=False)
    color = models.CharField(max_length=30, unique=False, blank=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.code, self.color)

    class Admin: 
        pass

class LargeWebfiles(models.Model):
    long_sku = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=50, unique=False, blank=False, null=False)
    mod_date = models.CharField(max_length=200, blank=True, null=True) 
    item_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)

    def __str__(self):
        return u'%s %s' % (self.long_sku, self.filename)

    class Admin: 
        pass


class RegularWebfiles(models.Model):
    long_sku = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=50, unique=False, blank=False, null=False)
    item_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)

    def __str__(self):
        return u'%s %s' % (self.long_sku, self.filename)

    class Admin: 
        pass

class MSWebfiles(models.Model):
    long_sku = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=50, unique=False, blank=False, null=False)
    item_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)

    def __str__(self):
        return u'%s %s' % (self.long_sku, self.filename)

    class Admin: 
        pass


class ThumbWebfiles(models.Model):
    long_sku = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=50, unique=False, blank=False, null=False)
    item_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=False, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=False, null=True)

    def __str__(self):
        return u'%s %s' % (self.long_sku, self.filename)

    class Admin: 
        pass


class PrintFile(models.Model):
    assoc_sku = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=500, blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    mod_date = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return u'%s %s' % (self.assoc_item_no, self.filename)

    class Admin: 
        pass



class OneImageFiles(models.Model):
    item_no = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filenames = models.ForeignKey(PrintFile)

    def __str__(self):
        return u'%s %s' % (self.item_no, self.filenames)

    class Admin: 
        pass

class Buyers(models.Model):
    buyer = models.CharField(max_length=50, null=True, blank=True)
    department = models.CharField(max_length=3, null=True, blank=True)
    product_class = models.CharField(max_length=4, unique=True, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.buyer, self.department, self.product_class, self.description)

    class Admin: 
        pass


class ProcessedFiles(models.Model):
    item_no = models.CharField(max_length=30, unique=False, blank=False, null=False)
    filename = models.CharField(max_length=50, unique=False, blank=True, null=True)
    processor = models.CharField(max_length=50, unique=False, blank=True, null=True)
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    product_class = models.CharField(max_length=10, unique=False, blank=True, null=True)
    upload_date = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.item_no, self.filename, self.processor, self.upload_date)

    class Admin: 
        pass


class Product(models.Model):
    ad_date = models.CharField(max_length=20, unique=False, blank=True, null=True, default=None)
    item_no = models.CharField(max_length=30, unique=True, blank=True, null=True)
    mfg = models.CharField(max_length=30, unique=False, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    vendor_number = models.CharField(max_length=30, unique=False, blank=True, null=True)
    order_date = models.DateField(null=True, blank=True)
    received_dc = models.DateField(null=True, blank=True)
    received_137 = models.CharField(max_length=30, unique=False, blank=True, null=True) 
    received_buyer = models.CharField(max_length=40, unique=False, blank=True, null=True)
    received_other = models.CharField(max_length=50, null=True, blank=True, default=None)
    photo_dldate = models.CharField(max_length=50, unique=False, blank=True, null=True)
    whowhen =  models.CharField(max_length=100, null=True, blank=True)
    studio_out = models.DateField(null=True, blank=True)
    checked_out =  models.CharField(max_length=100, null=True, blank=True)
    have_image = models.CharField(max_length=30, null=True, blank=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default='None')
    shooting_instructions = models.CharField(max_length=200, blank=True, null=True, default=None)
    studio_in = models.CharField(max_length=50, unique=False, blank=True, null=True) 
    notes = models.CharField(max_length=200, blank=True, null=True)
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    short_sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    from_file = models.CharField(max_length=30, null=True, blank=True)
    sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    first = models.CharField(max_length=5, unique=False, blank=True, null=True)
    first_date = models.CharField(max_length=30, null=True, blank=True)
    buyer = models.CharField(max_length=50, null=True, blank=True)
    # operator = models.CharField(max_length=50, null=True, blank=True)
    product_class = models.ForeignKey(Buyers, to_field='product_class')
    merch_to_137 = models.CharField(max_length=200, blank=True, null=True)
    dc_received_u = models.IntegerField(null=True, blank=True)
    curr_dc_oh_u = models.IntegerField(null=True, blank=True) 
    dc_curr_oo_u = models.IntegerField(null=True, blank=True) 
    na = models.CharField(max_length=5, unique=False, blank=True, null=True)
    size_type = models.CharField(max_length=10, unique=False, blank=True, null=True)
    color_desc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.item_no, ' ', self.desc)

    class Admin: 
        pass

class AdProduct(models.Model):
    ad_date = models.CharField(max_length=20, unique=False, blank=True, null=True, default=None)
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    mfg = models.CharField(max_length=30, unique=False, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    vendor_number = models.CharField(max_length=30, unique=False, blank=True, null=True)
    order_date = models.CharField(max_length=30, unique=False, blank=True, null=True)
    received_dc = models.CharField(max_length=30, unique=False, blank=True, null=True)
    received_137 = models.CharField(max_length=30, unique=False, blank=True, null=True) 
    received_buyer = models.CharField(max_length=40, unique=False, blank=True, null=True)
    received_other = models.CharField(max_length=50, null=True, blank=True, default=None)
    photo_dldate = models.CharField(max_length=50, unique=False, blank=True, null=True)
    whowhen =  models.CharField(max_length=100, null=True, blank=True)
    studio_out = models.CharField(max_length=30, unique=False, blank=True, null=True)
    checked_out =  models.CharField(max_length=100, null=True, blank=True)
    have_image = models.CharField(max_length=30, null=True, blank=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default='None')
    shooting_instructions = models.CharField(max_length=200, blank=True, null=True, default=None)
    studio_in = models.CharField(max_length=50, unique=False, blank=True, null=True) 
    notes = models.CharField(max_length=200, blank=True, null=True)
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    short_sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    from_file = models.CharField(max_length=30, null=True, blank=True)
    sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    first = models.CharField(max_length=5, unique=False, blank=True, null=True)
    first_date = models.CharField(max_length=30, null=True, blank=True)
    buyer = models.CharField(max_length=50, null=True, blank=True)
    merch_to_137 = models.CharField(max_length=200, blank=True, null=True)
    product_class = models.CharField(max_length=4, blank=True, null=True)
    dc_received_u = models.IntegerField(null=True, blank=True)
    curr_dc_oh_u = models.IntegerField(null=True, blank=True) 
    dc_curr_oo_u = models.IntegerField(null=True, blank=True)
    size_type = models.CharField(max_length=10, unique=False, blank=True, null=True) 
    na = models.CharField(max_length=5, unique=False, blank=True, null=True)
    size_type = models.CharField(max_length=10, unique=False, blank=True, null=True)
    color_desc = models.CharField(max_length=200, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.ad_date, ' ', self.item_no, ' ', self.desc)

    class Admin: 
        pass

class InventoryProduct(models.Model):
    sku = models.CharField(max_length=7, unique=False, blank=True, null=True)
    item_no = models.CharField(max_length=30, unique=True, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.CharField(max_length=3)
    source = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.sku, self.item_no, self.desc, self.quantity, self.source)

    class Meta:
        unique_together = ('sku', 'source',)

    class Admin: 
        pass


class RumbaProduct(models.Model):
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    mfg = models.CharField(max_length=30, unique=False, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    vendor_number = models.CharField(max_length=30, unique=False, blank=True, null=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default='None')
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    short_sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    product_class = models.CharField(max_length=4, blank=True, null=True)
    merch_to_137 = models.CharField(max_length=200, blank=True, null=True)
    dc_received_u = models.IntegerField(null=True, blank=True)
    curr_dc_oh_u = models.IntegerField(null=True, blank=True)
    dc_curr_oo_u = models.IntegerField(null=True, blank=True) 
    size_type = models.CharField(max_length=10, unique=False, blank=True, null=True)
    size = models.CharField(max_length=10, unique=False, blank=True, null=True)
    color_desc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return u'%s %s %s' % (self.item_no, ' ', self.desc)

    class Admin: 
        pass

class WatchedItem(models.Model):
    watched_by = models.ForeignKey(UserProfile, models.SET_NULL, blank=True, null=True)
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    desc = models.CharField(max_length=210, blank=True, null=True)
    comments = models.TextField(max_length=2000, blank=True, null=True) 
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.watched_by, self.item_no, self.desc, self.confirmed_placed, self.comments)

class HotItem(models.Model):
    item_no = models.CharField(max_length=30, unique=True, blank=False, null=False)
    ad_date = models.CharField(max_length=20, unique=False, blank=True, null=True, default=None)
    create_date = models.DateField(default=date.today)
    item_name = models.CharField(max_length=210, blank=True, null=True)
    comments = models.TextField(max_length=2000, blank=True, null=True) 
    reply = models.TextField(max_length=2000, blank=True, null=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default=None)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.create_date, self.item_no, self.item_name, self.confirmed_placed, self.comments)

class Deployed(models.Model):
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    operator = models.CharField(max_length=50, null=True, blank=True)
    filenames = JSONField()

    def __str__(self):
        return u'%s, %s' % (self.item_no, self.operator)

    class Admin: 
        pass  

class ReplacedImage(models.Model):
    sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    sku_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    old_filename = models.CharField(max_length=50, unique=False, blank=True, null=True)
    new_filename = models.CharField(max_length=50, unique=False, blank=True, null=True)
    processor = models.ForeignKey(UserProfile, blank=True, null=True)
    change_date = models.DateField(default=date.today, blank=True, null=True)


    def __str__(self):
        return u'%s %s %s %s %s %s' % (self.sku, self.item_no, self.old_filename, self.new_filename, self.processor, self.change_date)

    class Admin: 
        pass


class CheckProduct(models.Model):
    sku_ns = models.CharField(max_length=30)
    brand = models.CharField(max_length=20, unique=False, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default='None')
    ad_date = models.CharField(max_length=20, unique=False, blank=True, null=True)
    mfg = models.CharField(max_length=30, unique=False, blank=True, null=True)
    already_tracked = models.CharField(max_length=300, unique=False, blank=True, null=True, default='None')
    na = models.NullBooleanField(default=False)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.sku_ns, ' ', self.brand, ' ', self.desc)

    class Admin: 
        pass

class FirstReceipt(models.Model):
    buyer = models.CharField(max_length=30, null=True, blank=True)
    dc_received_u = models.IntegerField(null=True, blank=True)
    curr_dc_oh_u = models.IntegerField(null=True, blank=True) 
    dc_curr_oo_u = models.IntegerField(null=True, blank=True)
    date_received = models.CharField(max_length=20, unique=False, blank=True, null=True)
    item_ns = models.CharField(max_length=30, unique=False, blank=True, null=True)
    short_sku = models.CharField(max_length=30, unique=False, blank=True, null=True)
    size_type = models.CharField(max_length=10, unique=False, blank=True, null=True)
    item_no = models.CharField(max_length=30, unique=False, blank=True, null=True)
    vendor_style = models.CharField(max_length=30, unique=False, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    color_desc = models.CharField(max_length=200, blank=True, null=True)
    have_image = models.CharField(max_length=30, null=True, blank=True)
    ad_date = models.CharField(max_length=50, unique=False, blank=True, null=True)
    order_date = models.CharField(max_length=50, unique=False, blank=True, null=True)
    received_dc = models.CharField(max_length=30, unique=False, blank=True, null=True)
    received_137 = models.CharField(max_length=30, unique=False, blank=True, null=True)
    from_file = models.CharField(max_length=30, null=True, blank=True)
    photo_dldate = models.DateField(null=True, blank=True)
    whowhen =  models.CharField(max_length=100, null=True, blank=True)
    studio_out = models.CharField(max_length=50, unique=False, blank=True, null=True)
    checked_out =  models.CharField(max_length=100, null=True, blank=True)
    confirmed_placed = models.CharField(max_length=200, blank=True, null=True, default='None') 
    studio_in = models.CharField(max_length=50, unique=False, blank=True, null=True)
    merch_to_137 = models.CharField(max_length=200, blank=True, null=True)
    product_class = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.buyer, self.item_no, self.description, self.color_desc)

    class Admin: 
        pass



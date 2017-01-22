from django import forms
from multiupload.fields import MultiFileField
from django.forms import ModelForm, DateInput
from .models import *
from bootstrap3_datetime.widgets import DateTimePicker
import re
from django.forms.widgets import Widget, Select, MultiWidget
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory, BaseInlineFormSet, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field  


class PrdSearchForm(forms.Form): 
    query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32})
    ) 

class RecordSearchForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 
        
class PostsearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'size': 32})
    ) 
    def __init__(self, data=None, files=None, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'PostsearchForm'
        self.helper.form_method = 'get'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Field('query', placeholder=kwargs.pop('query_placeholder', 'enter query, date, or sku')),
        )
        super(PostsearchForm, self).__init__(data, files, **kwargs)

class ExportForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'size': 32})
    ) 
    def __init__(self, data=None, files=None, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'ExportForm'
        self.helper.form_method = 'get'
        self.helper.form_action = '.'

        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Field('query', placeholder=kwargs.pop('query_placeholder', 'what should I export?')),
        )
        super(ExportForm, self).__init__(data, files, **kwargs)

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = '__all__'


class FRForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = '__all__'   

class RIForm(forms.ModelForm):
    class Meta: 
        model = ReplacedImage
        fields = '__all__'    

# class HIForm(forms.ModelForm):
#     class Meta: 
#         model = HotItem
#         fields = '__all__'  

class PostSearchForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 

class ExportForm(forms.Form): 
  query = forms.CharField( 
      label='', 
      widget=forms.TextInput(attrs={'size': 32}) 
  ) 

ProductFormSetBase = modelformset_factory(
  Product, extra=0, fields=('ad_date', 'item_no', 'mfg', 'desc', 'order_date', 'received_dc', 'studio_out', 'confirmed_placed', 'na'))

AdProductFormSetBase = modelformset_factory(
  AdProduct, extra=0, fields=('ad_date', 'item_no', 'mfg', 'desc', 'order_date', 'received_dc', 'studio_out', 'confirmed_placed', 'na'))


FRFormSetBase = modelformset_factory(
  Product, extra=0, fields=("ad_date", "item_no", "mfg", "desc", "vendor_number", "order_date", "received_dc", "received_137", "received_buyer", "received_other", "photo_dldate", "whowhen", "studio_out", "checked_out", "have_image", "confirmed_placed", "shooting_instructions", "studio_in",  "notes", "item_ns", "short_sku", "from_file", "sku", "sku_ns", "first", "first_date", "buyer", "product_class", "merch_to_137", "dc_received_u", "curr_dc_oh_u", "dc_curr_oo_u", "na"))

RIFormSetBase = modelformset_factory(
  ReplacedImage, extra=0, fields=("sku", "sku_ns", "item_no",  "item_ns", "old_filename", "new_filename", "processor", "change_date"))

HIFormSetBase = modelformset_factory(
  HotItem, extra=0, fields=('item_no', 'ad_date', 'item_name', 'comments', 'reply', 'confirmed_placed'))

class ProductFormSet(ProductFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(ProductFormSet, self).add_fields(form, index)
    form.fields['is_checked'] = forms.BooleanField(required=False)
    # form.fields['somefield'].widget.attrs['class'] = 'somefieldclass'

class AdProductFormSet(AdProductFormSetBase):
  # this is where you can add additional fields to a ModelFormSet
  # this is also where you can change stuff about the auto generated form
  def add_fields(self, form, index):
    super(AdProductFormSet, self).add_fields(form, index)
    form.fields['is_checked'] = forms.BooleanField(required=False)
    # form.fields['somefield'].widget.attrs['class'] = 'somefieldclass'

class FRFormSet(FRFormSetBase):
  def add_fields(self, form, index):
    super(FRFormSet, self).add_fields(form, index)
    form.fields['is_checked'] = forms.BooleanField(required=False)

class HIFormSet(HIFormSetBase):
  def add_fields(self, form, index):
    super(HIFormSet, self).add_fields(form, index)
    form.fields['is_checked'] = forms.BooleanField(required=False)

class RIFormSet(RIFormSetBase):
  def add_fields(self, form, index):
    super(RIFormSet, self).add_fields(form, index)
    form.fields['is_checked'] = forms.BooleanField(required=False)

class WatchedItemForm(forms.ModelForm):
    class Meta:
        model = WatchedItem
        fields = '__all__'

class HotItemForm(forms.ModelForm):
    class Meta:
        model = HotItem
        # fields = '__all__'
        exclude = ['create_date']
        widgets = {'ad_date': DateInput(attrs={'class': 'datepicker'})}
        # def __init__(self, user_id, *args, **kwargs):
        # super(WatchedItemForm, self).__init__(*args, **kwargs)

        # # set the user_id as an attribute of the form
        # self.user_id = user_id

class MultiEntryForm(ModelForm):
    class Meta: 
        model = Product
        fields = [ 'ad_date', 'item_no', 'mfg', 'desc', 'order_date', 'received_dc', 'studio_out', 'confirmed_placed', 'na' ]

class BaseFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BasePlanItemFormSet, self).add_fields(form, index)
        # add fields to the form
        fields = [ 'ad_date', 'item_no', 'mfg', 'desc', 'order_date', 'received_dc', 'studio_out', 'confirmed_placed', 'na']
    
    def save_new(self, form, commit=True):
        # custom save behavior for new objects, form is a ModelForm
        return super(BaseFormSet, self).save_new(form, commit=commit)
 
    def save_existing(self, form, instance, commit=True):
        # custom save behavior for existing objects
        # instance is the existing object, and form has the updated data
        return super(BaseFormSet, self).save_existing(form, instance, commit=commit)

    # FormSet = inlineformset_factory(Product, formset=BaseFormSet)

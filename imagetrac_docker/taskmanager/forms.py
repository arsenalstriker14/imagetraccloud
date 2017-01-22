from django import forms
from django.forms import ModelForm, DateInput
from .models import InboxEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PrdInboxForm(ModelForm):
    class Meta:
        model = InboxEntry
        fields = '__all__'
        widgets = {'date_due': DateInput(attrs={'class': 'datepicker'}), 'completed_on': DateInput(attrs={'class': 'datepicker'})}
        


import sys
import os
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _

# Register your models here.


def in_progress(modeladmin, request, queryset):
    queryset.update(status='In Progress')
in_progress.short_description = "Mark selected projects as In Progress"

def holding(modeladmin, request, queryset):
    queryset.update(status='Posted')
holding.short_description = "Mark selected projects as Holding"

def completed(modeladmin, request, queryset):
    queryset.update(status='Completed')
completed.short_description = "Mark selected projects as Completed"

def awaiting_action(modeladmin, request, queryset):
    queryset.update(status='Awaiting Action')
awaiting_action.short_description = "Mark selected projects as Awaiting Action"

class InboxEntryAdmin(admin.ModelAdmin):
    list_display = ['job_name', 'priority', 'status']
    ordering = ['priority']
    actions = [completed, holding, in_progress, awaiting_action]


admin.autodiscover()

admin.site.register(InboxEntry, InboxEntryAdmin)
admin.site.register(TaskBox)
admin.site.register(InboxRequest)


def main():
    pass


if __name__ == '__main__':
    main()

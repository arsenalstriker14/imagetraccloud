from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from imagetrac_docker.b5.models import *
import django_filters
import datetime
from config.settings.common import UPLOAD_ROOT
from  django.core.files.storage import FileSystemStorage

upload_storage = FileSystemStorage(location=UPLOAD_ROOT, base_url='/uploads')


PRIORITY_CHOICES = (
    ('normal', 'normal'),
    ('low', 'low'),
    ('urgent', 'urgent'),    
)

STATUS_CHOICES = (
    ('Awaiting Action', 'Awaiting Action'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Holding for Response', 'Holding for Response'),
)
class InboxRequest(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return u'%s' % (self.name)

    class Admin:
        pass

class TaskBox(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    subscribers = models.ManyToManyField(UserProfile, related_name='member', blank=True)

    def __str__(self):
        return u'%s' % (self.name)

    class Admin:
        pass


class InboxEntry(models.Model):
        job_name = models.CharField(("Request (other)"), max_length=100, unique=False, blank=True, null=False)
        request = models.ForeignKey(InboxRequest, blank=True, null=True)
        priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default="Normal")
        date_in = models.DateField(("Date"), auto_now=True)
        date_due = models.DateField(("Requested date due"),auto_now=False)
        description = models.TextField(max_length=1000, unique=False, blank=True, null=True)
        reply = models.TextField(max_length=1000, unique=False, blank=True, null=True)
        assigned_by = models.ForeignKey(UserProfile, blank=False, null=False, default=User)
        box = models.ForeignKey(TaskBox, blank=True, null=True)
        assigned_to = models.ManyToManyField(UserProfile, related_name='name', blank=True)
        assigned_team = models.ManyToManyField(Department, blank=True)
        status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Awaiting Action")
        accepted_by = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True)
        completed_on = models.DateField(("Date completed"),auto_now=False, blank=True, null=True)
        attachment = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment2 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment3 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment4 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment5 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment6 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment7 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment8 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment9 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)
        attachment10 = models.FileField(upload_to='attachments/', storage=upload_storage, blank=True, null=True)

        def __str__(self):
            return u'%s %s %s %s' % (self.date_in, self.assigned_by, self.priority, self.job_name)

        class Admin: 
            pass
            
        class Meta:
            ordering = ['-priority', '-status']



            
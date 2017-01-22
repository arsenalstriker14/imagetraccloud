from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	url(r'^export_audit/', export_audit, name='export_audit'),
]

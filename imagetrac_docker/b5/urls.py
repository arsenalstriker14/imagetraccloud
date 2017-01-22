from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', ListCreateProducts.as_view(), name='product_list'),
    url(r'(?P<pk>\w+)/$', RetrieveUpdateDestroyProducts.as_view(), name='product_detail'),
    # url(r'^hotitems/', ListCreateHotItem.as_view(), name='hotitem_list'),
    url(r'^hotitems/(?P<pk>\w+)/$', RetrieveUpdateDestroyHotItem.as_view(), name='hotitem_detail'),
    # url(r'^v1/products/class', apiv1_products_class, name='apiv1_products_class'),
	url(r'^updateProduct/(?P<pk>\w+)/$', ProductUpdate.as_view(), name='update_entry'),
    url(r'^create-entry/', createEntry, name='createEntry'),
    url(r'^update-entry/(?P<id>\w+)/$', updateEntry, name='updateEntry'),
    url(r'^multipost/', multipost, name='multipost'),
    url(r'^multipost/(?P<ad_date>\w+)/', edit_multipost, name='edit_multipost'),
    url(r'^add_first/', add_first, name='add_first'),
    url(r'^replace_image/', replace_image, name='replace_image'),
    url(r'^view_replaced/', view_replaced, name='view_replaced'),
    url(r'^multipost-init/(?P<client>\w+)/(?P<id>\w+)/$', multipost_init, name='multipost-initial'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)
    urlpatterns += static(settings.PRINTMEDIA_URL, document_root=settings.PRINTMEDIA_ROOT)
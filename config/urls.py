# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.auth import views as auth_views

from django.views import i18n as django_views_i18n
from imagetrac_docker.b5.views import *
from imagetrac_docker.taskmanager.views import *

js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('imagetrac_docker.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'registration/password_change_form.html'}),
    # url(r'^accounts/', include('django.contrib.auth.urls')),

    # url(r'^api/v1/products/', include('imagetrac_docker.b5.urls', namespace='b5', app_name='b5')),
    # url(r'^$', login_user, name='login_user'),

    # url(r'^user/password/reset/$', auth_views.password_reset, {'post_reset_redirect' : '/user/password/reset/done/'},
    #     name="password_reset"),
    # url(r'^user/password/reset/done/$',auth_views.password_reset_done),
    # url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, {'post_reset_redirect' : '/user/password/done/'}),
    # url(r'^user/password/done/$', auth_views.password_reset_complete),


    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^main/', postsearch),
    url(r'^rumbasearch/', rumbasearch),
    url(r'^first/', frsearch),
    url(r'^adscreen/', adscreen),
    url(r'^pickup/', pickupsearch),
    url(r'^success/', success_message),
    url(r'^deployed/', record_deployed),
    url(r'^buyer-class/', buyer_class),
    url(r'^export/unavailable/', export_data, name="export"),
    url(r'^export/(.*)', export_data, name="export"),
    url(r'^export-daily/(.*)', export_daily, name="export_daily"),
    url(r'^export-mods/(.*)', export_mods, name="export_mods"),
    url(r'^export-pickup/(.*)', export_pickup, name="export_pickup"),
    url(r'^export-required/(.*)', export_required, name="export_required"),
    url(r'^export-studiocheck/', export_studiocheck, name="export_studiocheck"),
    url(r'^export-hotlist/(.*)', export_hotlist, name="export_hotlist"),
    url(r'^import/', import_data, name="import"),
    url(r'^import-fr/', import_first, name="import_first"),
    url(r'^import-check/', import_check, name="import_check"),
    url(r'^adminwatched/(?P<id>\w+)/', display_adminwatchlist, name='display_adminwatchlist'),
    url(r'^hotlist/', display_hotlist, name='display_hotlist'),
    url(r'^mywatched/(?P<id>\w+)/', display_watchlist, name='display_watchlist'),
    url(r'^quickcard/(?P<id>\w+)/', quickcard, name='quickcard'),
    url(r'^check_sequence/', check_sequence, name='check_sequence'),
    url(r'^docs/adsheet/', docs_adsheet, name='docs_adsheet'),
    url(r'^docs/daily/', docs_daily, name='docs_daily'),
    url(r'^docs/deploy/', docs_deploy, name='docs_deploy'),
    url(r'^docs/importer/', docs_importer, name='docs_importer'),
    url(r'^docs/inventory/', docs_inventory, name='docs_inventory'),
    url(r'^docs/restore/', docs_restore, name='docs_restore'),
    url(r'^docs/system/', docs_system, name='docs_system'),
    url(r'^edit_watcheditem/(?P<id>\w+)/(?P<userid>\w+)/', delete_watchlist_item, name='delete_watchlist_item'),
    url(r'^edit_adminwatched/(?P<id>\w+)/(?P<userid>\w+)/', delete_adminwatchlist_item, name='delete_adminwatchlist_item'),
    url(r'^edit_hotlist/(?P<id>\w+)/', delete_hotlist_item, name='delete_hotlist_item'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^logout/$', auth_views.logout, name='logout_page'),
    url(r'^analytics/', analytics, name="analytics"),
    url(r'^b5/', include('imagetrac_docker.b5.urls', namespace='b5', app_name='b5')),
    url(r'^taskmanager/', include('imagetrac_docker.taskmanager.urls', namespace="taskmanager")),
    url(r'^utilities/', include('imagetrac_docker.utilities.urls', namespace='utilities', app_name='utilities')),
    url(r'^product/(?P<sku>[A-Z0-9- ]+)/(?P<item_no>[A-Z0-9- ]+)', display_record, name="display_record"),
    url(r'^edit/', edit_view),
    url(r'^819/', inventory_819, name="inventory_819"),
    url(r'^studio_check/', studio_check),
    url(r'^exportcsv/', export_csv),
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^quicksearch/(?P<searchstring>[A-Za-z0-9 _@./#&+-]+)/', quicksearch, name="quicksearch"),
    url(r'^productsearch/(?P<searchstring>[A-Za-z0-9 _@./#&+-]+)/', productsearch, name="productsearch"),
    # url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^passwords/', include('password_reset.urls')), 
    url(r'^jsi18n$', django_views_i18n.javascript_catalog, js_info_dict),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
#  + static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT) + static(settings.PRINTMEDIA_URL, document_root=settings.PRINTMEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

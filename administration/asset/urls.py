from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from administration.models import Asset
from administration.asset.views import AssetCreateView, AssetUpdateView, AssetDeleteView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # index
                       url(r'^$', ListView.as_view(
                           model=Asset,
                           template_name='administration/asset/index.html',
                           context_object_name='assets'
                       )),

                       url(r'^ajax/add/$', permission_required('administration.add_asset', raise_exception=True)(
                           AssetCreateView.as_view()),
                           name='add_asset'),

                       url(r'^ajax/mod/(?P<asset>\d+)/',
                           permission_required('administration.change_asset', raise_exception=True)(
                               AssetUpdateView.as_view()),
                           name='change_asset'),

                       url(r'^ajax/delete/(?P<asset>\d+)/',
                           permission_required('administration.delete_asset', raise_exception=True)(
                               AssetDeleteView.as_view()),
                           name='delete_asset'),

                       # category
                       url(r'^category/', include('administration.asset.category.urls'))
)

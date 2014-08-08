from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from administration.models import Asset
from administration.asset.views import AssetCreateView, AssetUpdateView


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

                       url(r'^ajax/add/$', permission_required('administration.add_asset')(AssetCreateView.as_view())),

                       url(r'^ajax/mod/(?P<asset>\d+)/', permission_required('administration.change_asset')(AssetUpdateView.as_view())),

                       url(r'^ajax/delete/', 'administration.asset.views.asset_delete'),

                       # category
                       url(r'^category/', include('administration.asset.category.urls'))
)

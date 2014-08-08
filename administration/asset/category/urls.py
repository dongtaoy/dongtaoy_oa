from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from administration.models import AssetCategory
from administration.asset.category.views import AssetCategoryCreateView, AssetCategoryUpdateView, \
    AssetCategoryDeleteView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # index
                       url(r'^$', ListView.as_view(
                           model=AssetCategory,
                           template_name='administration/asset/category/index.html',
                           context_object_name='categories'
                       )),

                       # detail
                       url(r'^ajax/add/', permission_required('administration.add_assetcategory', raise_exception=True)(
                           AssetCategoryCreateView.as_view()), name='add_assetcategory'),

                       # save
                       url(r'^ajax/mod/(?P<category>\d+)/',
                           permission_required('administration.change_assetcategory', raise_exception=True)(
                               AssetCategoryUpdateView.as_view()), name='change_assetcategory'),


                       url(r'^delete/(?P<category>\d+)/',
                           permission_required('administration.delete_assetcategory', raise_exception=True)(
                               AssetCategoryDeleteView.as_view()), name='delete_assetcategory')


)

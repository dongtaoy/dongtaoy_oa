from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from masterdata.material.views import MaterialCreateView, MaterialUpdateView, MaterialDeleteView
from masterdata.models import Material

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    url(r'^type/', include('masterdata.material.type.urls')),

    # user url
    url(r'^$', (ListView.as_view(
        model=Material,
        context_object_name='materials',
        template_name='masterdata/material/index.html'))),


    url(r'^ajax/add/$',
        permission_required('masterdata.add_material', raise_exception=True)(MaterialCreateView.as_view()),
        name='add_material'),


    url(r'^ajax/mod/(?P<material>\d+)/$',
        permission_required('masterdata.change_material', raise_exception=True)(MaterialUpdateView.as_view()),
        name='change_material'),


    url(r'delete/(?P<material>\d+)/$',
        permission_required('masterdata.delete_material', raise_exception=True)(MaterialDeleteView.as_view()),
        name='delete_material'),


    # url(r'ajax/check/$', 'masterdata.material.views.user_check'),
)

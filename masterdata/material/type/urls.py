from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from masterdata.models import Material, MaterialType
from masterdata.material.type.views import MaterialTypeCreateView, MaterialTypeUpdateView, MaterialTypeDeleteView

urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(
                           model=MaterialType,
                           context_object_name='types',
                           template_name='masterdata/material/type/index.html')),

                       # detail
                       url(r'^ajax/add/', permission_required('masterdata.add_materialtype', raise_exception=True)(
                           MaterialTypeCreateView.as_view()), name='add_materialtype'),

                       # save
                       url(r'^ajax/mod/(?P<type>\d+)/',
                           permission_required('masterdata.change_materialtype', raise_exception=True)(
                               MaterialTypeUpdateView.as_view()), name='change_materialtype'),


                       url(r'^delete/(?P<type>\d+)/',
                           permission_required('masterdata.delete_materialtype', raise_exception=True)(
                               MaterialTypeDeleteView.as_view()), name='delete_materialtype')
)

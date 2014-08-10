from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from system.models import Label
from system.label.views import LabelCreateView, LabelUpdateView, LabelDeleteView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),

                       url(r'^$', ListView.as_view(
                           model=Label,
                           context_object_name='labels',
                           template_name='system/label/index.html')),

                       url(r'^ajax/add/$',
                           permission_required('system.add_label', raise_exception=True)(LabelCreateView.as_view()),
                           name='add_label'),


                       url(r'^ajax/mod/(?P<label>\d+)/$',
                           permission_required('system.change_label', raise_exception=True)(LabelUpdateView.as_view()),
                           name='change_label'),


                       url(r'^delete/(?P<label>\d+)/$',
                           permission_required('system.delete_label', raise_exception=True)(
                               LabelDeleteView.as_view(), ),
                           name='delete_label'),
)

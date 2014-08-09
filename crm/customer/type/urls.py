from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from system.models import Label
from crm.models import CustomerType, Customer
from crm.customer.type.views import CustomerTypeCreateView, CustomerTypeUpdateView,CustomerTypeDeleteView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),

                       #index
                       url(r'^$', ListView.as_view(
                           model=CustomerType,
                           context_object_name='types',
                           template_name='crm/customer/type/index.html')),

                       # detail
                       url(r'^ajax/add/', permission_required('crm.add_customertype', raise_exception=True)(
                           CustomerTypeCreateView.as_view()), name='add_customertype'),

                       # save
                       url(r'^ajax/mod/(?P<type>\d+)/',
                           permission_required('crm.change_customertype', raise_exception=True)(
                               CustomerTypeUpdateView.as_view()), name='change_customertype'),


                       url(r'^delete/(?P<type>\d+)/',
                           permission_required('crm.delete_customertype', raise_exception=True)(
                               CustomerTypeDeleteView.as_view()), name='delete_customertype')
)

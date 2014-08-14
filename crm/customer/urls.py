from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from crm.models import Customer
from crm.customer.views import CustomerCreateView, CustomerUpdateView,CustomerDeleteView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$','dongtaoy_oa.crm.views.customer_index'),
                       #url(r'^$', 'crm.customer.views.customer_index'),

                       #include
                       url(r'^type/', include('crm.customer.type.urls')),

                       # index
                       url(r'^$', ListView.as_view(
                           model=Customer,
                           template_name='crm/customer/index.html',
                           context_object_name='customers'
                       )),

                       url(r'^ajax/add/$', permission_required('crm.add_customer', raise_exception=True)(
                           CustomerCreateView.as_view()),
                           name='add_customer'),

                       url(r'^ajax/mod/(?P<customer>\d+)/$',
                           permission_required('crm.change_customer', raise_exception=True)(
                               CustomerUpdateView.as_view()),
                           name='change_customer'),

                       url(r'^delete/(?P<customer>\d+)/$',
                           permission_required('crm.delete_customer', raise_exception=True)(
                               CustomerDeleteView.as_view()),
                           name='delete_customer'),
)

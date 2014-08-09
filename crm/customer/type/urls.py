from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from system.models import Label
from crm.models import CustomerType,Customer
from crm.customer.type.views import CustomerTypeCreateView, CustomerTypeUpdateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    #index
    url(r'^$', ListView.as_view(
        model=Label,
        context_object_name='types',
        template_name='crm/customer/type/index.html')),

    url(r'^ajax/add/', permission_required('crm.add_label')(CustomerTypeCreateView.as_view())),


    url(r'^ajax/mod/(?P<type>\d+)', permission_required('crm.change_label')(CustomerTypeUpdateView.as_view())),


    url(r'^ajax/delete/', 'crm.customer.type.views.label_delete'),
)

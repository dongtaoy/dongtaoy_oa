from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from public.models import MessageType
from system.messagetype.views import MessageTypeCreateView, MessageTypeUpdateView, MessageTypeDeleteView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # index
                       url(r'^$', ListView.as_view(
                           model=MessageType,
                           template_name='public/message/type/index.html',
                           context_object_name='types'
                       )),

                       # detail
                       url(r'^ajax/add/$', permission_required('public.add_messagetype', raise_exception=True)(
                           MessageTypeCreateView.as_view()), name='add_messagetype'),

                       # save
                       url(r'^ajax/mod/(?P<type>\d+)/$',
                           permission_required('public.change_messagetype', raise_exception=True)(
                               MessageTypeUpdateView.as_view()), name='change_messagetype'),


                       url(r'^delete/(?P<type>\d+)/$',
                           permission_required('public.delete_messagetype', raise_exception=True)(
                               MessageTypeDeleteView.as_view()), name='delete_messagetype')


)

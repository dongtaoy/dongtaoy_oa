from django.conf.urls import patterns, include, url
from public.announcement.views import AnnouncementCreateView


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # announcement url
    url(r'^publish/', AnnouncementCreateView.as_view()),

    #url(r'^ajax/save/', 'public.announcement.views.announcement_save')

)

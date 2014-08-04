from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # announcement url
    url(r'^publish/', 'public.announcement.views.announcement_publish_index'),
    url(r'^ajax/save/', 'public.announcement.views.announcement_save')

)

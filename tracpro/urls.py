from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^manage/', include('dash.orgs.urls')),
    url(r'^manage/', include('dash.dashblocks.urls')),
    url(r'^manage/', include('dash.stories.urls')),
    url(r'^manage/', include('dash.categories.urls')),
    url(r'^users/', include('dash.users.urls')),
    url(r'', include('tracpro.supervisors.urls')),
    url(r'', include('tracpro.chat.urls')),
    url(r'', include('tracpro.home.urls')),
    url(r'', include('tracpro.contacts.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = patterns('',
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

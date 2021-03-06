from django.conf.urls import patterns, url

urlpatterns = patterns('app.event.views',
    url('^$', 'index', name='events'),

    url('^api/register/(?P<id>\d+)/$', 'register', name='register'),
    url('^api/register/(?P<id>\d+)/(?P<team_id>[a-f0-9]{5})/$', 'register', name='register'),

    url('^api/unregister/(?P<id>\d+)/$', 'unregister', name='unregister'),
    url('^api/unregister/(?P<id>\d+)/(?P<team_id>[a-f0-9]{5})/$', 'unregister', name='unregister'),

    url('^(?P<slug>[-\w]+)/', 'details', name='event_details')
)

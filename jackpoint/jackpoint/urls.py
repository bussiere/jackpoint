from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jackpoint.views.home', name='home'),
    # url(r'^Jackpoint/', include('Jackpoint.foo.urls')),
    url(r'^$', 'jackpoint.engine.views.index'),
    #url(r'^X/$', 'jackpoint.X.views.index'),
    url(r'^invitation/$', 'jackpoint.invitation.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^invitation/create_invitation/$', 'jackpoint.invitation.views.create_invitation'),
    url(r'^invitation/inscription/$', 'jackpoint.invitation.views.invitation_inscription'),
    url(r'^invitation/inscription/validation/$', 'jackpoint.invitation.views.validation_inscription'),
    url(r'^hand/$', 'jackpoint.hand.views.index'),
    url(r'^X/$', 'jackpoint.X.views.index'),
    url(r'^hand/ask/$', 'jackpoint.hand.views.ask'),
    url(r'^hand/view/$','jackpoint.hand.views.index'),
    url(r'^hand/view/(?P<id>\d+)/$','jackpoint.hand.views.viewid'),
    url(r'^mp/(?P<id>\d+)/$','jackpoint.mp.views.index'),
    url(r'^jack/view/(?P<id>\d+)/$','jackpoint.jack.views.viewid'),
    url(r'^jack/edit/$','jackpoint.jack.views.editJack'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from solid_i18n.urls import solid_i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = solid_i18n_patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^alogin/', include('alogin.urls')),
    url(r'^sa/', include('social_auth.urls')),
    url(r'^feedback/', include('backfeed.urls')),
    url(r'^stationtime/', include('stationtime.urls')),
    url(r'^remotelink/', include('remotelink.urls')),

)

urlpatterns += patterns('',
    url(r'^api/', include('project.urls_api')),
    url(r'^', include('contentproxy.urls')),
    url(r'^subscription/', include('subscription.urls')),
)

urlpatterns += solid_i18n_patterns('',
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
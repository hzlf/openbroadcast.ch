from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from django.conf.urls import patterns, url
from .views import SubscribeView, WebhookView

urlpatterns = [
    # site integration
    url(r'^subscribe/(?P<list_id>[-\w]+)/$', SubscribeView.as_view(), name='subscription-subscribe'),
    # webhooks
    url(r'^webhook/(?P<backend>[-\w]+)/(?P<token>[-\w]+)/$', WebhookView.as_view(), name='subscription-mailchimp-webhook'),
]

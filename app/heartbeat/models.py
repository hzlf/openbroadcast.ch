# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.conf import settings
from django.utils import timezone
from django.db import models

log = logging.getLogger(__name__)

User = settings.AUTH_USER_MODEL


class Beat(models.Model):

    user = models.OneToOneField(User, related_name="beat", on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta(object):
        app_label = "heartbeat"
        verbose_name = "Beat"
        ordering = ("-updated",)

    def __str__(self):
        return "{0} {1}".format(self.user.username, self.updated)

    @property
    def last_beat(self):
        if self.updated:
            return timezone.now() - self.updated

    def save(self, *args, **kwargs):
        super(Beat, self).save(*args, **kwargs)

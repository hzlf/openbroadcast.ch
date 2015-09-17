from __future__ import absolute_import

from .celery import app as celery_app

__all__ = ['celery_app']

def update_permissions_after_migration(app,**kwargs):
    """
    Update app permission just after every migration.
    This is based on app django_extensions update_permissions management command.
    """
    from django.conf import settings
    from django.db.models import get_app, get_models
    from django.contrib.auth.management import create_permissions

    create_permissions(get_app(app), get_models(), 2 if settings.DEBUG else 0)

#post_migrate.connect(update_permissions_after_migration)




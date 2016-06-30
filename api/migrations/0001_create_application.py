# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 00:15
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

def create_application(apps, schema_editor):
    from oauth2_provider.models import Application as ActualApplication
    Application = apps.get_model('oauth2_provider', 'Application')
    ShareUser = apps.get_model('share', 'ShareUser')
    share_user = ShareUser.objects.get(username=settings.APPLICATION_USERNAME)
    fields = dict(
        client_type=str(ActualApplication.CLIENT_TYPES[0][1]),
        authorization_grant_type=str(ActualApplication.GRANT_TYPES[2][1]),
        name='Harvester API',
        user=share_user
    )
    oauth_app = Application.objects.create(**fields)

class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
        ('share', '0002_create_share_user'),
    ]

    operations = [
        migrations.RunPython(create_application),
    ]

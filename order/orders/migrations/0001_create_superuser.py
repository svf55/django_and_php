# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('admin')
    superuser.save()


def delete_superuser(apps, schema_editor):
    superuser = User.objects.get(username='admin')
    superuser.delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=delete_superuser)
    ]

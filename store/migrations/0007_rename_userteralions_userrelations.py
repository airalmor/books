# Generated by Django 4.1.7 on 2023-03-14 06:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_userteralions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTeralions',
            new_name='UserRelations',
        ),
    ]

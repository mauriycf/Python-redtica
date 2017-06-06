# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('age', models.CharField(max_length=100, blank=True)),
                ('cellphone', models.CharField(max_length=100, blank=True)),
                ('address', models.CharField(max_length=100, blank=True)),
                ('job_info', models.CharField(max_length=100, blank=True)),
                ('education', models.CharField(max_length=100, blank=True)),
                ('biography', models.CharField(max_length=300, blank=True)),
                ('social_network', models.CharField(max_length=100, blank=True)),
                ('avatar_image', models.FileField(upload_to='static/avatar/')),
                ('id_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

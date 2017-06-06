# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170525_1502'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]

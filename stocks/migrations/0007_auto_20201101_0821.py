# Generated by Django 2.2.12 on 2020-11-01 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_auto_20201101_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_assets',
            old_name='company_ids',
            new_name='company_id',
        ),
    ]

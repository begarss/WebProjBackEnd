# Generated by Django 3.0.4 on 2020-04-26 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200426_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='user',
            new_name='author',
        ),
    ]

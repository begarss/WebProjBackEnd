# Generated by Django 3.0.5 on 2020-04-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=False, max_length=300, null=True),
        ),
    ]

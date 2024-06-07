# Generated by Django 5.0.6 on 2024-05-27 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm_net_app', '0007_alter_organization_email'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='moderator',
            field=models.BooleanField(default=False, verbose_name='Moderator'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='comm_net_app.organization', verbose_name='Organization'),
        ),
    ]

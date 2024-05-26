# Generated by Django 5.0.6 on 2024-05-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comm_net_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='supplier',
        ),
        migrations.AddField(
            model_name='organization',
            name='supplier',
            field=models.ManyToManyField(null=True, to='comm_net_app.organization', verbose_name='Supplier'),
        ),
    ]

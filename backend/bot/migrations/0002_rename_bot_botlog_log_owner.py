# Generated by Django 4.0.5 on 2022-08-31 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botlog',
            old_name='bot',
            new_name='log_owner',
        ),
    ]

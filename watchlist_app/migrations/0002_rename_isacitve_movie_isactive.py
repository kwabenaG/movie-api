# Generated by Django 3.2.8 on 2021-10-26 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='IsAcitve',
            new_name='IsActive',
        ),
    ]
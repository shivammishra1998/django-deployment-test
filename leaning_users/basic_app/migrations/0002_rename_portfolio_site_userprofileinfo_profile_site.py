# Generated by Django 4.0.4 on 2022-05-06 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_site',
            new_name='profile_site',
        ),
    ]
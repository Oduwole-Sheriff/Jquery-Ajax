# Generated by Django 4.2.13 on 2024-06-15 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jquery_ajax_app', '0006_remove_profile_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
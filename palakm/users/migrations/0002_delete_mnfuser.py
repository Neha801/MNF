# Generated by Django 3.0.5 on 2020-12-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('socialaccount', '0003_extra_data_default_dict'),
        ('account', '0002_email_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MNFUser',
        ),
    ]

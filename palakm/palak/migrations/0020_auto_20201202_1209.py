# Generated by Django 3.0.5 on 2020-12-02 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palak', '0019_auto_20201201_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character_edit',
            old_name='selection',
            new_name='music',
        ),
    ]

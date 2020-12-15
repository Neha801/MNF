# Generated by Django 3.0.5 on 2020-11-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palak', '0002_auto_20201125_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script_info',
            old_name='location',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='script_info',
            old_name='type_of_script',
            new_name='script_written_in',
        ),
        migrations.AddField(
            model_name='script_info',
            name='city',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Mumbai', 'Mumbai')], default='Mixed', max_length=20),
        ),
    ]
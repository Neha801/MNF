# Generated by Django 3.0.5 on 2020-11-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palak', '0011_auto_20201128_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script_info',
            name='upload',
        ),
        migrations.AddField(
            model_name='script_info',
            name='scriptfile',
            field=models.FileField(default='', upload_to='scriptfile'),
        ),
    ]

# Generated by Django 3.0.5 on 2020-12-01 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palak', '0017_auto_20201130_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='character_edit',
            name='character_image',
            field=models.ImageField(default='', upload_to='character_image'),
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-27 12:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('djangocms_slider', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SliderItem',
            new_name='Slide',
        ),
    ]

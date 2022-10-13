# Generated by Django 3.2.15 on 2022-10-01 07:36

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='background_section_backgroundsection', serialize=False, to='cms.cmsplugin')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название блока')),
                ('background_color', colorfield.fields.ColorField(blank=True, default='#00BB00', help_text='Опция будет проигнорирована, если задано фоновое изображение', image_field=None, max_length=18, null=True, samples=None, verbose_name='Фоновый цвет')),
                ('background_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Фоновое изображение')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
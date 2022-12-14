# Generated by Django 3.2.15 on 2022-09-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_colorblocks', '0005_auto_20220928_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colorblock',
            options={'ordering': ('order',), 'verbose_name': 'цветной блок', 'verbose_name_plural': 'цветные блоки'},
        ),
        migrations.AddField(
            model_name='colorblock',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]

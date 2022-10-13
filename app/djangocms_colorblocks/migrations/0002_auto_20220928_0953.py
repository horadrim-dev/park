# Generated by Django 3.2.15 on 2022-09-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_colorblocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorblock',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colorblock',
            name='icon',
            field=models.CharField(blank=True, default='', help_text='Названия иконок брать <a href="https://icons.getbootstrap.com/" target=\\_blank">отсюда</a>', max_length=32, null=True, verbose_name='Иконка'),
        ),
    ]
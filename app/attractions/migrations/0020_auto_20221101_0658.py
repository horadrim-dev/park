# Generated by Django 3.2.15 on 2022-11-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0019_attraction_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='work_in_summer',
            field=models.BooleanField(default=True, verbose_name='Летний сезон'),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='work_in_winter',
            field=models.BooleanField(default=False, verbose_name='Зимний сезон'),
        ),
    ]
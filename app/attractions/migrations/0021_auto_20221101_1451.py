# Generated by Django 3.2.15 on 2022-11-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0020_auto_20221101_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='work_in_summer',
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='work_in_winter',
        ),
        migrations.AddField(
            model_name='attraction',
            name='season',
            field=models.CharField(choices=[('summer', 'Лето'), ('winter', 'Зима')], default='summer', max_length=16, verbose_name='Сезон'),
        ),
    ]

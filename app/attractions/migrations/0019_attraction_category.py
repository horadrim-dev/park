# Generated by Django 3.2.15 on 2022-10-28 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0018_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attractions.category'),
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-28 10:42

import adminsortable.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_colorblocks', '0003_remove_colorblock_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colorblock',
            options={'ordering': ('block_order',), 'verbose_name': 'цветной блок', 'verbose_name_plural': 'цветные блоки'},
        ),
        migrations.AddField(
            model_name='colorblock',
            name='block_order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='colorblock',
            name='plugin',
            field=adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangocms_colorblocks.colorblocksmodel'),
        ),
    ]

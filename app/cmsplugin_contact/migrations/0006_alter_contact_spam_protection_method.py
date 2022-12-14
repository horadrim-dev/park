# Generated by Django 3.2.15 on 2022-11-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_contact', '0005_alter_contact_spam_protection_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='spam_protection_method',
            field=models.SmallIntegerField(choices=[(0, 'Honeypot'), (1, 'Akismet'), (2, 'ReCAPTCHA V2')], default=0, verbose_name='Spam protection method'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-29 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name_plural': 'Families'},
        ),
    ]

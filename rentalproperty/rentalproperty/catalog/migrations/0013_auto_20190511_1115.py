# Generated by Django 2.2 on 2019-05-11 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_area_rent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['endOfRental'], 'permissions': (('can_mark_rent', 'Set area as free'),)},
        ),
    ]
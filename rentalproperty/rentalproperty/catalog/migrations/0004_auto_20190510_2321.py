# Generated by Django 2.2 on 2019-05-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190427_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typearea',
            name='name',
            field=models.CharField(blank=True, choices=[('office', 'office'), ('stock', 'stock'), ('shopping center', 'shopping_center')], default='office', max_length=2),
        ),
    ]
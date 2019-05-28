# Generated by Django 2.2 on 2019-04-27 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('of', 'office'), ('st', 'stock'), ('sc', 'shopping_center')], default='of', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.CharField(help_text='Площадь помещения', max_length=100)),
                ('price', models.CharField(help_text='Цена', max_length=100)),
                ('year', models.DateField(blank=True, null=True)),
                ('floor', models.IntegerField(help_text='На каком этаже находится помещение', max_length=100)),
                ('communication', models.TextField(help_text='Вода, отопление,электрическтво')),
                ('address', models.TextField(help_text='Где находится')),
                ('status', models.CharField(blank=True, choices=[('f', 'Free'), ('b', 'Busy')], default='f', max_length=1)),
                ('typeArea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.TypeArea')),
            ],
        ),
    ]

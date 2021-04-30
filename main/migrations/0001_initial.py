# Generated by Django 3.1.7 on 2021-04-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vac_center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('centerid', models.IntegerField()),
                ('vaccines_av', models.IntegerField()),
                ('update', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('mobno', models.IntegerField(unique=True)),
                ('state', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('timeslot', models.CharField(max_length=256)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vac_center')),
            ],
        ),
    ]

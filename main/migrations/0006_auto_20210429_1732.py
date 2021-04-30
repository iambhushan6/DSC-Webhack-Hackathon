# Generated by Django 3.1.7 on 2021-04-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210429_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='state',
            field=models.CharField(choices=[('Maharashtra', 'Maharashtra')], max_length=256),
        ),
        migrations.AlterField(
            model_name='vac_center',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur')], max_length=256),
        ),
        migrations.AlterField(
            model_name='vac_center',
            name='state',
            field=models.CharField(choices=[('Maharashtra', 'Maharashtra')], max_length=256),
        ),
    ]
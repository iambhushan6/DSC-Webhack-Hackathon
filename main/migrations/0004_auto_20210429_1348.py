# Generated by Django 3.1.7 on 2021-04-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210428_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='city',
            field=models.CharField(choices=[('Nagpur', 'Nagpur'), ('Mumbai', 'Mumbai'), ('Pune', 'Pune')], max_length=256),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='state',
            field=models.CharField(choices=[('Gujrat', 'Gujrat'), ('Maharashtra', 'Maharashtra')], max_length=256),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210430_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur')], max_length=256),
        ),
        migrations.AlterField(
            model_name='vac_center',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur')], max_length=256),
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
# Generated by Django 3.2.5 on 2021-09-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
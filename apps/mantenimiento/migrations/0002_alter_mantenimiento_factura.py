# Generated by Django 3.2.5 on 2022-03-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='factura',
            field=models.ManyToManyField(blank=True, null=True, to='mantenimiento.Factura'),
        ),
    ]

# Generated by Django 3.2.5 on 2023-03-17 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20230317_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='codigoProducto',
        ),
    ]
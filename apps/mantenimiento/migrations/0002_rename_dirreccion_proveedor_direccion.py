# Generated by Django 3.2.5 on 2023-03-26 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='dirreccion',
            new_name='direccion',
        ),
    ]
# Generated by Django 3.2.5 on 2023-04-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_remove_detallefactura_codigoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

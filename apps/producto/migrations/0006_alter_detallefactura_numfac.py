# Generated by Django 3.2.5 on 2023-04-01 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_alter_factura_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='numFac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.factura'),
        ),
    ]

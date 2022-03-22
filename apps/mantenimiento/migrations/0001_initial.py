# Generated by Django 3.2.5 on 2022-03-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Empresas',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numFac', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('moneda', models.CharField(choices=[('CORDOBAS', 'CORDOBAS'), ('DOLARES', 'DOLARES')], max_length=100, null=True)),
                ('iva', models.FloatField()),
                ('subTotal', models.FloatField()),
                ('total', models.FloatField()),
                ('tipoCambio', models.FloatField()),
                ('formaPago', models.CharField(choices=[('TRANSFERENCIA', 'TRANSFERENCIA'), ('CHEQUE', 'CHEQUE'), ('EFECTIVO', 'EFECTIVO'), ('TARJETA', 'TARJETA')], max_length=100, null=True)),
                ('detalle', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Factura',
            },
        ),
        migrations.CreateModel(
            name='Mant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Mantenimientos',
                'verbose_name_plural': 'Mantenimientos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('ruc', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(max_length=100, null=True)),
                ('dirreccion', models.CharField(max_length=100, null=True)),
                ('formaPago', models.CharField(choices=[('DE CONTADO', 'DE CONTADO'), ('Credito', 'Credito')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorizado', models.CharField(max_length=100, null=True)),
                ('realizado', models.CharField(max_length=100, null=True)),
                ('comentario', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateField()),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.empresa')),
                ('factura', models.ManyToManyField(to='mantenimiento.Factura')),
                ('mant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.mant')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.proveedor'),
        ),
    ]

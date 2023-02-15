# Generated by Django 3.2.5 on 2022-03-22 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('vehiculo', models.CharField(choices=[('Motocicleta', 'Motocicleta'), ('Microbus', 'Microbus'), ('Camioneta', 'Camioneta'), ('Carro', 'Carro')], max_length=100, null=True)),
                ('combustible', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel')], max_length=100, null=True)),
                ('asignar', models.CharField(max_length=100, null=True)),
                ('modelo', models.CharField(max_length=100, null=True)),
                ('rendimiento', models.FloatField()),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('factura', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('monto', models.FloatField()),
                ('litros', models.FloatField()),
                ('km_inicio', models.FloatField()),
                ('km_fin', models.FloatField()),
                ('vehiculo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='combustible.vehiculo')),
            ],
            options={
                'verbose_name': 'Registro Vehicular',
                'verbose_name_plural': 'Registro Vehicular',
            },
        ),
    ]
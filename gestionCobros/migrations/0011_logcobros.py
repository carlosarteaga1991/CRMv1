# Generated by Django 3.0.8 on 2020-08-02 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionCobros', '0010_codigos_gestiones_motivos_pagos_promesas_recordatorios'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogCobros',
            fields=[
                ('id_log', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tabla', models.CharField(max_length=35)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_registro', models.IntegerField(blank=True, null=True)),
                ('tipo_accion', models.CharField(choices=[('Insertar', 'Insertar'), ('Modificar', 'Modificar'), ('Seleccionar', 'Seleccionar'), ('Borrar', 'Borrar')], max_length=35, verbose_name='Tipo de Acción')),
                ('Dato_anterior', models.CharField(blank=True, max_length=400)),
                ('Dato_despues', models.CharField(blank=True, max_length=400)),
                ('campo_afectado', models.CharField(blank=True, max_length=35)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionCobros.Clientes')),
            ],
            options={
                'verbose_name_plural': 'Bitácora App Cobros',
                'ordering': ['fecha'],
            },
        ),
    ]

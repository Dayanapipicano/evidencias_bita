# Generated by Django 5.0.5 on 2024-06-27 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateField(auto_now=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('identificacion', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.cargo')),
                ('id_dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.dependencia')),
                ('id_rol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.rol')),
                ('id_tipo_documento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.tipodocumento')),
            ],
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-14 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_cliente_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Combustible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_combustible', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('kilometraje', models.IntegerField()),
                ('precio', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.categoria')),
                ('combustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.combustible')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.estado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fotografia', models.ImageField(blank=True, upload_to='')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.vehiculo')),
            ],
        ),
    ]

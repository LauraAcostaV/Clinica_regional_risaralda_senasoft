# Generated by Django 3.2.4 on 2021-10-22 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('documento_identidad', models.IntegerField()),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('celular', models.CharField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('documento_identidad', models.IntegerField()),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('celular', models.CharField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('especialidad', models.CharField(choices=[('Pe', 'Pediatra'), ('Fa', 'Farmaceuta'), ('UCI', 'Unidad de cuidados intensivos'), ('Ge', 'Medico General')], default='Ge', max_length=35)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=20)),
                ('Contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('enfermero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.enfermeros')),
                ('especialista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cedula de Extrangeria')], default='CC', max_length=30)),
                ('documento', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Modified', models.DateTimeField(auto_now=True)),
                ('enfermero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.enfermeros')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.especialista')),
            ],
        ),
        migrations.AddField(
            model_name='enfermeros',
            name='especialista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.especialista'),
        ),
    ]

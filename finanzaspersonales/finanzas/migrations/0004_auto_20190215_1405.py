# Generated by Django 2.1.7 on 2019-02-15 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_gestionegresos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuenteIngreso',
            fields=[
                ('id', models.AutoField(help_text='ID Fuente de Ingreso', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('estado', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', help_text='Estado Fuente de Ingreso', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='GestionIngresos',
            fields=[
                ('id', models.AutoField(help_text='ID Gestion de Egresos', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Descripcion', max_length=50, verbose_name='Descripcion')),
                ('estado', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', help_text='Estado del tipo de pago', max_length=1, verbose_name='Estado')),
                ('fuente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.FuenteIngreso', verbose_name='Fuente de Ingreso')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.TipoIngresos', verbose_name='Tipo de Egreso')),
            ],
        ),
        migrations.AlterField(
            model_name='gestionegresos',
            name='descripcion',
            field=models.CharField(help_text='Descripcion', max_length=50, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='gestionegresos',
            name='estado',
            field=models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', help_text='Estado del tipo de pago', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='gestionegresos',
            name='renglon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.RenglonEgresos', verbose_name='Renglon'),
        ),
        migrations.AlterField(
            model_name='gestionegresos',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.TipoEgresos', verbose_name='Tipo de Egreso'),
        ),
        migrations.AlterField(
            model_name='gestionegresos',
            name='tipopago',
            field=models.ForeignKey(default='X', null=True, on_delete=django.db.models.deletion.SET_NULL, to='finanzas.TipoPago', verbose_name='Tipo de pago'),
        ),
    ]

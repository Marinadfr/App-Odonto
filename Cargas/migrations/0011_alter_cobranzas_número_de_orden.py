# Generated by Django 4.2 on 2023-05-11 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cargas', '0010_cobranzas_número_de_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobranzas',
            name='Número_de_orden',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cargas.presupuestos'),
        ),
    ]

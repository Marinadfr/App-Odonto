# Generated by Django 4.2 on 2023-05-11 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cargas', '0015_remove_presupuestos_número_de_comprobante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cobranzas',
            old_name='Número_de_orden',
            new_name='Número_de_orden_relación',
        ),
        migrations.RemoveField(
            model_name='cobranzas',
            name='Orden',
        ),
    ]

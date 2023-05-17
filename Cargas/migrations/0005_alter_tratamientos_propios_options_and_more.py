# Generated by Django 4.2 on 2023-05-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cargas', '0004_tratamientos_obrassociales_prepagas_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tratamientos_propios',
            options={'ordering': ['Código_interno'], 'verbose_name_plural': 'Tratamientos Propios'},
        ),
        migrations.AlterField(
            model_name='tratamientos_obrassociales_prepagas',
            name='Código',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tratamientos_obrassociales_prepagas',
            name='Tratamiento',
            field=models.CharField(max_length=50),
        ),
    ]

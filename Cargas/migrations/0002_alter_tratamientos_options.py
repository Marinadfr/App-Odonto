# Generated by Django 4.2 on 2023-05-16 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cargas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tratamientos',
            options={'ordering': ['Tipo'], 'verbose_name_plural': 'Tratamientos'},
        ),
    ]

# Generated by Django 2.2.5 on 2020-03-02 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['apellido', 'nombre'], 'verbose_name_plural': 'Autores'},
        ),
    ]

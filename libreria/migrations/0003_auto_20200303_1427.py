# Generated by Django 2.2.5 on 2020-03-03 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_auto_20200302_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='genero',
        ),
        migrations.AddField(
            model_name='libro',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libreria.Genero'),
        ),
    ]
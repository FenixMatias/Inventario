# Generated by Django 3.0.8 on 2020-07-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20200707_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(max_length=5000),
        ),
    ]

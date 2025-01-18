# Generated by Django 4.2.11 on 2024-05-09 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSNAT', '0012_rename_cantidad_extra_ingrediente_cantidad_porcion_extra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='unidad',
            field=models.CharField(choices=[('gramos', 'Gramos'), ('onzas', 'Onzas')], default='gramos', max_length=10),
        ),
    ]

# Generated by Django 4.2.11 on 2024-05-09 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSNAT', '0014_rename_is_available_bebida_disponible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

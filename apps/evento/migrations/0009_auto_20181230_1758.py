# Generated by Django 2.1.1 on 2018-12-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0008_auto_20181230_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistente',
            name='identificador',
            field=models.CharField(max_length=12, verbose_name='Numero Identificador'),
        ),
    ]

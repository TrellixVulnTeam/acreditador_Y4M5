# Generated by Django 2.1.1 on 2019-01-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0012_auto_20181231_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['-fecha'], 'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]

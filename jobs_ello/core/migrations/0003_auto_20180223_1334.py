# Generated by Django 2.0.2 on 2018-02-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180223_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='codigo_exercicio',
            field=models.IntegerField(max_length=10, verbose_name='Cogigo exercicio'),
        ),
        migrations.AlterField(
            model_name='mandato',
            name='codigo_mandato',
            field=models.IntegerField(max_length=10, verbose_name='Codigo Mandato'),
        ),
        migrations.AlterField(
            model_name='parlamentar',
            name='codigo_do_parlamentar',
            field=models.IntegerField(max_length=10, verbose_name='Codigo Parlamentar'),
        ),
        migrations.AlterField(
            model_name='suplente',
            name='codigo_suplente',
            field=models.IntegerField(max_length=10, verbose_name='codigo parlamentar'),
        ),
    ]

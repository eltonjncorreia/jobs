# Generated by Django 2.0.2 on 2018-02-23 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suplente',
            old_name='codigo_parlamentar',
            new_name='codigo_suplente',
        ),
    ]

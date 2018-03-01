# Generated by Django 2.0.2 on 2018-02-27 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_mandato_uf_parlamentar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legislacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_legislatura', models.IntegerField(blank=True, null=True, verbose_name='Codigo legislatura')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Data Inicio')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data Fim')),
            ],
        ),
        migrations.RemoveField(
            model_name='mandato',
            name='data_fim',
        ),
        migrations.RemoveField(
            model_name='mandato',
            name='data_inicio',
        ),
        migrations.RemoveField(
            model_name='mandato',
            name='nome_legislatura',
        ),
        migrations.RemoveField(
            model_name='mandato',
            name='numero_legislatura',
        ),
        migrations.AddField(
            model_name='legislacao',
            name='mandato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legislacoes', to='core.Mandato'),
        ),
    ]

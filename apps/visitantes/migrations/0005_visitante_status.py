# Generated by Django 3.0 on 2024-01-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0004_auto_20240122_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColinaDoSol', '0003_business_alter_store_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatinghours',
            name='lunch_end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Fim de almoço'),
        ),
        migrations.AlterField(
            model_name='operatinghours',
            name='lunch_start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Início de almoço'),
        ),
        migrations.AlterField(
            model_name='operatinghours',
            name='weekday',
            field=models.CharField(choices=[('segunda', 'Segunda-feira'), ('terca', 'Terça-feira'), ('quarta', 'Quarta-feira'), ('quinta', 'Quinta-feira'), ('sexta', 'Sexta-feira'), ('sabado', 'Sábado'), ('domingo', 'Domingo'), ('feriados', 'Feriados')], max_length=10),
        ),
    ]
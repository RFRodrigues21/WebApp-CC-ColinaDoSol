# Generated by Django 4.2.1 on 2023-06-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColinaDoSol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='business',
            field=models.CharField(choices=[('pastelaria', 'Pastelaria'), ('doces_cafes', 'Doces e Cafés'), ('papelaria_tabacaria', 'Papelaria/Tabacaria'), ('telecomunicacoes_reparacoes', 'Telecomunicações/Reparações'), ('ocupacao_sazonal', 'Ocupação Sazonal'), ('supermercado', 'Supermercado'), ('restaurante_chines', 'Restaurante Chinês'), ('chaves_expresso', 'Chaves Expresso'), ('ginasio_cultura_lazer', 'Ginásio/Cultura e Lazer'), ('acessorios_idosos', 'Acessórios para Idosos'), ('moda_vestuario_langerie', 'Moda e Vestuário/Lingerie'), ('ginasio_reabilitacao', 'Ginásio e Reabilitação')], max_length=256, verbose_name='Ramo de Atividade'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_num',
            field=models.IntegerField(unique=True),
        ),
    ]
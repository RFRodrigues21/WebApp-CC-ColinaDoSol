# Generated by Django 4.2.2 on 2023-06-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColinaDoSol', '0005_siteconfiguration_sliderimage_alter_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebookLink',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Link do Facebook'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='instagramLink',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Link do Instagram'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo',
            field=models.ImageField(default='ColinaDoSol/static/ColinaDoSol/img/LogoCoresH.png', upload_to='content/ColinaDoSol/img/'),
        ),
    ]

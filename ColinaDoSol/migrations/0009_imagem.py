# Generated by Django 4.2.2 on 2023-06-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColinaDoSol', '0008_delete_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='uploads/products')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ordem', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
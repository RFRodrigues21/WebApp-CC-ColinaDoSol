from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.staticfiles import finders
from .models import Imagem


@receiver(post_migrate)
def create_default_image(sender, **kwargs):
    if Imagem.objects.count() == 0:
        default_image_path = 'ColinaDoSol/img/CSOL-WEBSITE_BANNErS-Preview02.jpg'
        default_image = Imagem(imagem=default_image_path, ordem=0)

        # Get the absolute path of the image using finders
        abs_image_path = finders.find(default_image_path)

        # Open and assign the image file to the ImageField
        with open(abs_image_path, 'rb') as image_file:
            default_image.imagem.save(default_image_path, image_file, save=True)

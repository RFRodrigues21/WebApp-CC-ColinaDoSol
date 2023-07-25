import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class Business(models.Model):
    business = models.CharField(max_length=100)

    def __str__(self):
        return self.business


def get_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f"id{instance.store_num}{ext}"
    return os.path.join('storeLogo/', filename)


class Store(models.Model):
    store_num = models.IntegerField(unique=True)
    image = models.ImageField(upload_to=get_image_path)
    brand = models.CharField('Nome loja', max_length=256)
    business = models.ForeignKey(Business, on_delete=models.DO_NOTHING, null=True)
    phoneNum = models.CharField('Contacto telefónico', max_length=12)
    email = models.CharField('E-mail', max_length=256)
    description = models.TextField('Descrição da loja')
    facebookLink = models.CharField('Link do Facebook', max_length=256, null=True, blank=True)
    instagramLink = models.CharField('Link do Instagram', max_length=256, null=True, blank=True)
    linkedinLink = models.CharField('Link do Linkedin', max_length=256, null=True, blank=True)
    twitterLink = models.CharField('Link do Twitter', max_length=256, null=True, blank=True)
    websiteLink = models.CharField('Link do Website', max_length=256, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand


class OperatingHours(models.Model):
    WEEKDAYS = (
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
        ('feriados', 'Feriados')
    )

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=10, choices=WEEKDAYS)
    opening_time = models.TimeField('Horario de abertura', null=True, blank=True)
    closing_time = models.TimeField('Horario de fecho', null=True, blank=True)
    lunch_start_time = models.TimeField('Início de almoço', null=True, blank=True)
    lunch_end_time = models.TimeField('Fim de almoço', null=True, blank=True)



class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=128)
    description = models.CharField('Descrção', max_length=512)
    image = models.ImageField(upload_to='uploads/products')


class UserAction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=1100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.action} {self.date}'


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        LOJISTA = "LOJISTA", 'Lojista'

    role = models.CharField(max_length=100, choices=Role.choices)
    phone_number = models.CharField(max_length=20, blank=True)
    is_first_login = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class SiteConfiguration(models.Model):
    logo = models.ImageField(upload_to='content/ColinaDoSol/img/')
    description = models.TextField()
    facebookLink = models.CharField('Link do Facebook', max_length=256, null=True, blank=True)
    instagramLink = models.CharField('Link do Instagram', max_length=256, null=True, blank=True)


class Imagem(models.Model):
    imagem = models.ImageField(upload_to='uploads/products')
    timestamp = models.DateTimeField(auto_now_add=True)
    ordem = models.PositiveIntegerField(default=0)


class AccessToken(models.Model):
    token = models.CharField(max_length=255)


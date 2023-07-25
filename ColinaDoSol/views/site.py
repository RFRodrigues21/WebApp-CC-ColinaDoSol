import os
import random

from django.core.mail import send_mail


from ColinaDoSol.forms import ContactForm
from ColinaDoSol.models import Store, SiteConfiguration, Imagem, AccessToken
from django.shortcuts import render, redirect
import requests
import datetime


def mapa(request):
    lojasList = Store.objects.all()
    return render(request, 'ColinaDoSol/mapa.html', {'lojasList': lojasList})


def index(request):
    lojasList = Store.objects.all()
    lojasList = lojasList.order_by('?')
    form = ContactForm()
    content = SiteConfiguration.objects.first()

    imagesList = Imagem.objects.all().order_by('ordem')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # send email
            recipient_email = [os.environ.get('DEFAULT_FROM_EMAIL')]
            subject_email = f'Email de {name} - {subject}'
            message_email = f'De: {name} - {email} \n assunto: {subject} \n mensagem: {message} '

            send_mail(subject_email, message_email, os.environ.get('DEFAULT_FROM_EMAIL'), recipient_email)

    # Retrieve access token from the database or .env file
    try:
        access_token = AccessToken.objects.get()
    except AccessToken.DoesNotExist:
        access_token = os.environ.get('INSTA_ACCESS_TOKEN')

    # Verify if token needs to be refreshed
    refresh_url = f"https://graph.instagram.com/refresh_access_token"
    refresh_params = {
        "grant_type": "ig_refresh_token",
        "access_token": access_token
    }
    refresh_response = requests.get(refresh_url, params=refresh_params)
    refresh_data = refresh_response.json()

    if 'expires_in' in refresh_data:
        expires_in = refresh_data['expires_in']
        current_time = datetime.datetime.now().timestamp()
        expiration_time = current_time + expires_in

        # Compare expiration time with a week from now
        week_in_seconds = 7 * 24 * 60 * 60
        if expiration_time <= current_time + week_in_seconds:
            # Token needs to be refreshed
            access_token = refresh_data['access_token']
            # Update the access token in the database or .env file

    url = "https://graph.instagram.com/me/media"
    params = {
        "fields": "caption,media_url,thumbnail_url,timestamp,media_type,id,permalink",
        "access_token": access_token
    }

    response = requests.get(url, params=params)
    data = response.json()
    posts = data.get('data', [])
    posts = posts[:3]

    urlFb = "https://graph.facebook.com/v17.0/me"
    paramsFb = {
        "fields": "id,posts{icon,full_picture,message,created_time,link,type,attachments{media}}",
        "access_token": os.environ.get('FB_ACCESS_TOKEN')
    }

    headers = {
        "Accept": "application/json"
    }

    responseFb = requests.get(urlFb, params=paramsFb, headers=headers)
    dataFb = responseFb.json()
    postsFb = dataFb.get('posts', {}).get('data', [])
    postsFb = postsFb[:3]

    for post in posts:
        timestamp = post['timestamp']
        date = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z").date()
        formatted_date = date.strftime("%d-%m-%Y")
        post['formatted_date'] = formatted_date

    for postFb in postsFb:
        createdDate = postFb['created_time']
        date = datetime.datetime.strptime(createdDate, "%Y-%m-%dT%H:%M:%S%z").date()
        formatted_date = date.strftime("%d-%m-%Y")
        postFb['created_time'] = formatted_date


    context = {
        'lojasList': lojasList,
        'form': form,
        'content': content,
        'images': imagesList,
        'posts': posts,
        'postsFb': postsFb,

    }

    return render(request, 'ColinaDoSol/index.html', context)


def custom_404_view(request, exception):
    return redirect("ColinaDoSol:index")


def get_access_token():
    token_obj, created = AccessToken.objects.get_or_create(pk=1)
    return token_obj.token


def set_access_token(token):
    token_obj, created = AccessToken.objects.get_or_create(pk=1)
    token_obj.token = token
    token_obj.save()

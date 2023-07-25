import os

from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ColinaDoSol.decorators import admin_required
from ColinaDoSol.models import Announcement, UserAction
from ColinaDoSol.views.user import get_user_emails


def dboard_anuncios(request):
    anuncios = Announcement.objects.all()
    return render(request, 'ColinaDoSol/Dashboard/Anuncios/dboard-anuncios.html',
                  {'anuncios': anuncios, 'current_page': 'anuncios'})


@admin_required
def dboard_novo_anuncio(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')

        anuncio = Announcement(title=title, text=text, user=request.user)

        # send email
        recipient_email = get_user_emails()
        subject = f'Anuncio - {title}'
        message = f'{text}'

        send_mail(subject, message, os.environ.get('DEFAULT_FROM_EMAIL'), recipient_email)

        anuncio.save()

        action = 'Criou um novo anuncio {}'.format(anuncio.title)
        user_action = UserAction(user=request.user, action=action)
        user_action.save()

        anuncios = Announcement.objects.all()

        context = {
            'anuncios': anuncios,
            'current_page': 'anuncios'
        }

        return render(request, 'ColinaDoSol/Dashboard/Anuncios/dboard-anuncios.html', context)
    return render(request, 'ColinaDoSol/Dashboard/Anuncios/dboard-novo-anuncio.html', {'current_page': 'anuncios'})


@admin_required
def dboard_editar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Announcement, id=anuncio_id)
    user = request.user

    if user.role != user.Role.ADMIN and anuncio.user != user:
        raise Http404("This page does not exist")

    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')

        changed_fields = []

        old_values = {}  # Store old values here

        if anuncio.title != title:
            changed_fields.append('title')
            old_values['title'] = anuncio.title  # Store old value of 'title'
            anuncio.title = title

        if anuncio.text != text:
            changed_fields.append('text')
            old_values['text'] = anuncio.text  # Store old value of 'text'
            anuncio.text = text

        anuncio.save()

        if changed_fields:
            change_logs = []
            for field in changed_fields:
                change_logs.append(
                    "Campo '{}' alterado: '{}' -> '{}'".format(field, old_values[field], getattr(anuncio, field)))

            action = 'Editou o anuncio {} - {}'.format(anuncio.title, ', '.join(change_logs))
            user_action = UserAction(user=request.user, action=action)
            user_action.save()

        return redirect('ColinaDoSol:dboard_anuncios')

    context = {
        'anuncio': anuncio,
        'current_page': 'anuncios'
    }

    return render(request, 'ColinaDoSol/Dashboard/Anuncios/dboard-editar-anuncio.html', context)


@admin_required
def dboard_delete_anuncio(request, anuncio_id):
    anuncio = Announcement.objects.get(id=anuncio_id)
    action = 'Eliminou o anuncio {}'.format(anuncio.title)
    user_action = UserAction(user=request.user, action=action)
    user_action.save()
    anuncio.delete()

    return HttpResponseRedirect(reverse('ColinaDoSol:dboard_anuncios'))

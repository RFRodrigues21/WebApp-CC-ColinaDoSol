import os

from django.contrib import messages
from django.contrib.admin.models import LogEntry
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ColinaDoSol.decorators import admin_required
from ColinaDoSol.models import User, UserAction


@admin_required
def dboard_novo_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        # password = request.POST.get('password')
        password = User.objects.make_random_password()
        role_name = request.POST.get('role')

        if role_name == "ADMIN":
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                role=User.Role.ADMIN
            )
        else:
            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                role=User.Role.LOJISTA
            )

        # send email
        recipient_email = [email]
        subject = 'Novo utilizador'
        message = f'Foi criado um novo utilizador com o username {username} e a password {password}.' \
                  f' \n ***Terá de alterar a sua password ao fazer o primeiro login***'

        send_mail(subject, message, os.environ.get('DEFAULT_FROM_EMAIL'), recipient_email)

        user.is_active = True
        user.set_password(password)
        user.save()

        action = 'Criou um novo utilizador {} com privilégios de {}'.format(user.username, user.role)
        user_action = UserAction(user=request.user, action=action)
        user_action.save()

        admins = User.objects.filter(role=User.Role.ADMIN)
        lojistas = User.objects.filter(role=User.Role.LOJISTA)

        context = {
            'admins': admins,
            'lojistas': lojistas,
            'current_page': 'lojistas'
        }

        return render(request, 'ColinaDoSol/Dashboard/Users/dboard-lojistas.html', context)
    return render(request, 'ColinaDoSol/Dashboard/Users/dboard-novo-user.html', {'current_page': 'lojistas'})


@login_required
def dboard_editar_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # user = User.objects.get(id=request.user.id)

    utilizador = request.user

    if utilizador.role != utilizador.Role.ADMIN and not utilizador.is_superuser and utilizador.id != user.id:
        raise Http404("This page does not exist")

    if request.method == "POST":

        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')

        changes = []

        if user.first_name != new_first_name:
            changes.append(f"<strong>Primeiro Nome:</strong> {user.first_name} -> {new_first_name}")

        if user.last_name != new_last_name:
            changes.append(f"<strong>Ultimo nome:</strong> {user.last_name} -> {new_last_name}")

        if user.username != new_username:
            changes.append(f"<strong>Ultimo nome:</strong> {user.username} -> {new_username}")

        if user.email != new_email:
            changes.append(f"<strong>Ultimo nome:</strong> {user.email} -> {new_email}")

        user.first_name = new_first_name
        user.last_name = new_last_name
        user.username = new_username
        user.email = new_email

        user.save()

        action = 'Editou o user {} e alterou os seguintes campos:<br>&emsp; {}'.format(user.username,
                                                                                       '<br>&emsp;'.join(changes))
        user_action = UserAction(user=request.user, action=action)
        user_action.save()

        if utilizador.role != utilizador.Role.ADMIN:
            return redirect('ColinaDoSol:dboard_lojistas')

        else:
            return redirect('ColinaDoSol:dboard_perfil')

    context = {
        'user': user,
        'current_page': 'lojistas'
    }
    return render(request, 'ColinaDoSol/Dashboard/Users/dboard-editar-lojista.html', context)


@login_required()
def user_reset_password(request):
    user = request.user
    form = SetPasswordForm(user=request.user)

    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            # new_password = form.cleaned_data['new_password']

            # user.set_password(str(new_password))
            form.save()
            user.is_first_login = False
            user.save()

            recipient_email = [user.email]
            subject_email = f'Alteração de palavra passe'
            message_email = f'A sua password foi alterada com sucesso'

            send_mail(subject_email, message_email, os.environ.get('DEFAULT_FROM_EMAIL'), recipient_email)

            login(request, user)

            return redirect('ColinaDoSol:dboard_main')
        else:
            print(form.errors)

            for field in form:
                print(f"Field: {field.name}")
                if field.errors:
                    for error in field.errors:
                        print(f"Error: {error}")

    context = {
        'user': User,
        'form': form,
    }
    return render(request, 'ColinaDoSol/setPassword.html', context)


@admin_required
def dboard_delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    action = 'Eliminou o user {} - {}'.format(user.username, user.role)
    user_action = UserAction(user=request.user, action=action)
    user_action.save()
    user.delete()

    return HttpResponseRedirect(reverse('ColinaDoSol:dboard_lojistas'))


@login_required()
def dboard_perfil(request):
    user = request.user
    # logs = UserAction.objects.all()
    logs = LogEntry.objects.all()

    context = {
        'user': user,
        'logs': logs,
        'current_page': 'perfil'

    }

    return render(request, 'ColinaDoSol/Dashboard/Users/dboard-perfil.html', context)


@admin_required
def dboard_lojistas(request):
    admins = User.objects.filter(role=User.Role.ADMIN)
    lojistas = User.objects.filter(role=User.Role.LOJISTA)

    context = {
        'admins': admins,
        'lojistas': lojistas,
        'current_page': 'lojistas'

    }

    return render(request, 'ColinaDoSol/Dashboard/Users/dboard-lojistas.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_first_login:
                return redirect('ColinaDoSol:dboard_reset_pass')

            return redirect('ColinaDoSol:dboard_main')
        else:
            messages.error(request, "Credenciais Inválidas!")
            return redirect('ColinaDoSol:login')
    else:
        return render(request, 'ColinaDoSol/loginPage.html')


def logout_user(request):
    if request.user.is_authenticated:
        action = 'Fez logout'
        user_action = UserAction(user=request.user, action=action)
        user_action.save()
    logout(request)
    return redirect('ColinaDoSol:index')


def get_user_emails():
    users = User.objects.all()
    emails = [user.email for user in users]
    return emails


@admin_required
def dboard_logs(request):
    logs = UserAction.objects.all()

    context = {
        'logs': logs,
        'current_page': 'logs'
    }

    return render(request, 'ColinaDoSol/Dashboard/Logs/Logs.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ColinaDoSol.models import Announcement, User, Store


@login_required
def dboard_main(request):
    anunciosList = Announcement.objects.all()

    if request.user.role == User.Role.ADMIN or request.user.is_superuser:
        lojasList = Store.objects.all()
        lojistas = User.objects.filter(role=User.Role.LOJISTA)
        context = {'lojasList': lojasList[:3], 'lojistas': lojistas[:3], 'anuncios': anunciosList, 'current_page': 'dashboard'}

    else:
        lojasList = Store.objects.filter(user=request.user)
        context = {'lojasList': lojasList[:3], 'anuncios': anunciosList, 'current_page': 'dashboard'}
    return render(request, 'ColinaDoSol/Dashboard/dboard-main.html', context)

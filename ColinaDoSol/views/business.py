from django.shortcuts import get_object_or_404, redirect, render

from ColinaDoSol.forms import BusinessForm
from ColinaDoSol.models import Business, UserAction


def businesses(request):
    businessList = Business.objects.all()
    success_message = ""

    if request.method == 'POST':
        if 'business_id' in request.POST:
            # Edit existing business
            business_id = request.POST.get('business_id')
            business = get_object_or_404(Business, id=business_id)
            form = BusinessForm(request.POST, instance=business)
            if form.is_valid():
                form.save()
                success_message = "Ramo editado com sucesso!"


                return redirect('ColinaDoSol:businesses')  # Redirect after successful form submission
        else:
            form = BusinessForm(request.POST)
            if form.is_valid():
                business = form.save()

                action = 'Eliminou o ramo de negocio {}'.format(business.business)
                user_action = UserAction(user=request.user, action=action)
                user_action.save()

                success_message = "Ramo criado com sucesso!"
                return redirect('ColinaDoSol:businesses')  # Redirect after successful form submission
    else:
        form = BusinessForm()

    context = {
        'form': form,
        'businessList': businessList,
        'success_message': success_message,
        'current_page': 'ramos'
    }
    return render(request, 'ColinaDoSol/Dashboard/Ramos/ramos-atividade.html', context)


def delete_business(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    business.delete()

    action = 'Eliminou o ramo de negocio {}'.format(business.business)
    user_action = UserAction(user=request.user, action=action)
    user_action.save()

    return redirect('ColinaDoSol:businesses')

import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from ColinaDoSol.forms import StoreForm, OperatingHoursForm, ProductsForm
from ColinaDoSol.models import Store, Product, OperatingHours, UserAction


@login_required
def dboard_lojas(request):
    if request.user.role == "ADMIN" or request.user.is_superuser:
        lojasList = Store.objects.all()
        productList = Product.objects.all()
    else:
        lojasList = Store.objects.filter(user=request.user)
        productList = Product.objects.filter(store__in=lojasList)

    context = {
        'productList': productList,
        'lojasList': lojasList,
        'current_page': 'lojas'

    }
    return render(request, 'ColinaDoSol/Dashboard/Lojas/dboard-lojas.html', context)


@login_required
def dboard_nova_loja(request):
    if request.method == 'POST':
        store_form = StoreForm(request.POST, request.FILES)
        operating_hours_forms = []

        if store_form.is_valid():
            store = store_form.save()

            for weekday, _ in OperatingHours.WEEKDAYS:
                form = OperatingHoursForm(request.POST, prefix=weekday, initial={'weekday': weekday})
                if form.is_valid():
                    operating_hours = form.save(commit=False)
                    operating_hours.store = store
                    operating_hours.save()
                    operating_hours_forms.append(form)

            action = 'Criou a loja nº {} - {}'.format(store.store_num, store.brand)
            user_action = UserAction(user=request.user, action=action)
            user_action.save()

            return redirect('ColinaDoSol:dboard_lojas')
    else:
        store_form = StoreForm()

    operating_hours_forms = [
        OperatingHoursForm(prefix=weekday, initial={'weekday': weekday})
        for weekday, _ in OperatingHours.WEEKDAYS
    ]

    context = {
        'store_form': store_form,
        'operating_hours_forms': operating_hours_forms,
        'current_page': 'lojas'

    }

    return render(request, 'ColinaDoSol/Dashboard/Lojas/dboard-nova-loja.html', context)


@login_required
def dboard_editar_loja(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    operating_hours = OperatingHours.objects.filter(store=store).order_by('id')
    storeImage = store.image.path

    if request.method == 'POST':
        store_form = StoreForm(request.POST, request.FILES, instance=store)
        operating_hours_forms = []

        if store_form.is_valid():
            if 'image' in request.FILES:
                storeImage = storeImage.replace('\\', '/')
                if os.path.isfile(storeImage):
                    os.remove(storeImage)

            store = store_form.save()

            # Registro de log
            action = 'Editou a loja {}: \n'.format(store.brand)
            change_logs = []

            for field in store_form.changed_data:
                old_value = store_form.initial.get(field)
                new_value = store_form.cleaned_data.get(field)
                change_logs.append(" Campo '{}': '{}' -> '{}'<br>".format(field, old_value, new_value))

            horario_alterado = False

            for weekday, _ in OperatingHours.WEEKDAYS:
                prefix = weekday
                form = OperatingHoursForm(request.POST, prefix=prefix)

                if form.is_valid():
                    opening_time = form.cleaned_data['opening_time']
                    closing_time = form.cleaned_data['closing_time']

                    lunch_start_time = form.cleaned_data['lunch_start_time']
                    lunch_end_time = form.cleaned_data['lunch_end_time']

                    if opening_time and closing_time:
                        operating_hour, created = OperatingHours.objects.get_or_create(store=store, weekday=weekday)
                        operating_hour.opening_time = opening_time
                        operating_hour.closing_time = closing_time
                        operating_hour.lunch_start_time = lunch_start_time
                        operating_hour.lunch_end_time = lunch_end_time

                        operating_hour.save()
                        operating_hours_forms.append(form)

                        if form.has_changed():
                            horario_alterado = True

            if horario_alterado:
                change_logs.append("Horario alterado <br>")

            if change_logs:
                action += '\n'.join(change_logs)
                user_action = UserAction(user=request.user, action=action)
                user_action.save()

            return redirect('ColinaDoSol:dboard_lojas')

    else:
        store_form = StoreForm(instance=store)
        operating_hours_forms = [
            OperatingHoursForm(prefix=operating_hour.weekday, instance=operating_hour)
            for operating_hour in operating_hours
        ]

    context = {
        'store': store,
        'store_form': store_form,
        'operating_hours_forms': operating_hours_forms,
        'current_page': 'lojas'
    }

    return render(request, 'ColinaDoSol/Dashboard/Lojas/dboard-editar-loja.html', context)


@login_required
def dboard_delete_loja(request, store_id):
    store = Store.objects.get(id=store_id)
    action = 'Eliminou a loja nº {} - {}'.format(store.store_num, store.brand)
    user_action = UserAction(user=request.user, action=action)
    user_action.save()
    store.delete()
    os.remove(store.image.path)

    return HttpResponseRedirect(reverse('ColinaDoSol:dboard_lojas'))


def dboard_new_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            product = form.save()

            action = 'Criou o prodto {} para a loja nº {} - {}'.format(product.name, product.store.store_num,
                                                                       product.store.brand)
            user_action = UserAction(user=request.user, action=action)
            user_action.save()
            return redirect('ColinaDoSol:dboard_lojas')
    else:
        form = ProductsForm(user=request.user)
        context = {
            'form': form,
            'current_page': 'lojas'
        }
        return render(request, 'ColinaDoSol/Dashboard/Products/dboard-novo-produto.html', context)


def dboard_edit_product(request, produto_id):
    product = get_object_or_404(Product, pk=produto_id)

    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance=product, user=request.user)
        if form.is_valid():
            form.save()

            # Registro de log
            action = 'Editou o produto {}:'.format(product.name)
            change_logs = []

            for field in form.changed_data:
                old_value = form.initial.get(field)
                new_value = form.cleaned_data.get(field)
                change_logs.append("Campo '{}' alterado: '{}' -> '{}'".format(field, old_value, new_value))

            action += ', '.join(change_logs)

            user_action = UserAction(user=request.user, action=action)
            user_action.save()

            return redirect('ColinaDoSol:dboard_lojas')
    else:
        form = ProductsForm(instance=product, user=request.user)

    context = {
        'form': form,
        'product': product,
        'current_page': 'lojas'
    }
    return render(request, 'ColinaDoSol/Dashboard/Products/dboard-editar-produto.html', context)


def dboard_delete_product(request, produto_id):
    produto = get_object_or_404(Product, pk=produto_id)
    action = 'Eliminou o produto {} da loja {}'.format(produto.name, produto.store.brand)
    user_action = UserAction(user=request.user, action=action)
    user_action.save()
    produto.delete()
    os.remove(produto.image.path)

    return HttpResponseRedirect(reverse('ColinaDoSol:dboard_lojas'))

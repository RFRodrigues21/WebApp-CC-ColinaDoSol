from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ColinaDoSol.models import SiteConfiguration, Imagem
from ColinaDoSol.forms import SiteConfigurationForm, ImagemForm


@login_required
def edit_content(request):
    site_settings_obj = SiteConfiguration.objects.first()  # Assuming there is only one SiteSettings object

    if request.method == 'POST':
        form = SiteConfigurationForm(request.POST, request.FILES, instance=site_settings_obj)
        if form.is_valid():
            form.save()

            return redirect('ColinaDoSol:content')  # Redirect to the homepage or any desired URL after saving
    else:
        form = SiteConfigurationForm(instance=site_settings_obj)
    return render(request, 'ColinaDoSol/Dashboard/SiteContent/content_edit.html',
                  {'form': form, 'current_page': 'conteudos'})


@login_required
def content(request):
    site_content = SiteConfiguration.objects.first()
    imagens = Imagem.objects.all().order_by('ordem')

    return render(request, 'ColinaDoSol/Dashboard/SiteContent/content.html',
                  {'content': site_content, 'current_page': 'conteudos', 'imagens': imagens})


@login_required
def sliderImagesList(request):
    imagens = Imagem.objects.all().order_by('ordem')

    return render(request, 'ColinaDoSol/Dashboard/SiteContent/imagensLista.html',
                  {'imagens': imagens, 'current_page': 'conteudos'})


from django.http import JsonResponse


@login_required
def atualizar_ordem(request):
    if request.method == 'POST':
        nova_ordem = request.POST.getlist('ordem[]')  # Obter a nova ordem dos itens da requisição POST

        for posicao, imagem_id in enumerate(nova_ordem):
            imagem = Imagem.objects.get(id=imagem_id)
            imagem.ordem = posicao
            imagem.save()

        # Retornar uma resposta JSON indicando sucesso
        data = {'success': True}
        return JsonResponse(data)

    # Se a requisição não for do tipo POST, retornar uma resposta JSON indicando erro
    data = {'success': False, 'error': 'Método inválido'}
    return JsonResponse(data)


@login_required
def adicionar_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)

            # Definir a ordem da nova imagem
            imagem.ordem = Imagem.objects.count()

            imagem.save()

            # Atualizar a posição de todas as imagens
            imagens = Imagem.objects.all().order_by('ordem')
            for posicao, imagem in enumerate(imagens):
                imagem.ordem = posicao
                imagem.save()

            return redirect('ColinaDoSol:sliderImagesList')

    else:
        form = ImagemForm()

    return render(request, 'ColinaDoSol/Dashboard/SiteContent/addImagemLista.html',
                  {'form': form, 'current_page': 'conteudos'})


@login_required
def excluir_imagem(request, imagem_id):
    imagem = get_object_or_404(Imagem, id=imagem_id)
    ordem_atual = imagem.ordem

    imagem.delete()

    # Atualizar a ordem após a exclusão
    imagens = Imagem.objects.filter(ordem__gt=ordem_atual).order_by('ordem')
    for posicao, imagem in enumerate(imagens, start=ordem_atual):
        imagem.ordem = posicao
        imagem.save()

    return redirect('ColinaDoSol:sliderImagesList')

from django.urls import path, reverse_lazy

from django.contrib.auth import views as auth_views
from .views.site import *
from .views.business import *
from .views.user import *
from .views.store import *
from .views.anuncios import *
from .views.dashboard import *
from .views.content import *

app_name = 'ColinaDoSol'

urlpatterns = [
    path('', index, name='index'),
    path('mapa', mapa, name='mapa'),
    path('dashboard/', dboard_main, name='dboard_main'),
    path('dashboard/perfil/resetPass', user_reset_password, name='dboard_reset_pass'),
    path('dashboard/perfil', dboard_perfil, name='dboard_perfil'),
    path('dashboard/lojistas', dboard_lojistas, name='dboard_lojistas'),
    path('dashboard/novoUser', admin_required(dboard_novo_user), name='dboard_novo_user'),
    path('dashboard/lojas', dboard_lojas, name='dboard_lojas'),
    path('dashboard/anuncios', dboard_anuncios, name='dboard_anuncios'),
    path('dashboard/novaLoja', admin_required(dboard_nova_loja), name='dboard_nova_loja'),
    path('dashboard/novoProduto', dboard_new_product, name='dboard_novo_produto'),
    path('dashboard/editarProduto/<int:produto_id>', dboard_edit_product, name='dboard_editar_produto'),
    path('dashboard/deleteProduto/<int:produto_id>', dboard_delete_product, name='dboard_delete_produto'),
    path('dashboard/novoAnuncio', admin_required(dboard_novo_anuncio), name='dboard_novo_anuncio'),
    path('dashboard/editarAnuncio/<int:anuncio_id>', dboard_editar_anuncio, name='dboard_editar_anuncio'),
    path('dashboard/deleteAnuncio/<int:anuncio_id>', dboard_delete_anuncio, name='dboard_delete_anuncio'),
    path('dashboard/editar/<int:store_id>', dboard_editar_loja, name='dboard_editar_loja'),
    path('dashboard/deleteUser/<int:user_id>', dboard_delete_user, name='dboard_delete_user'),
    path('dashboard/editarUser/<int:user_id>', dboard_editar_user, name='dboard_editar_lojista'),
    path('dashboard/delete/<int:store_id>', dboard_delete_loja, name='dboard_delete_loja'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('businesses', businesses, name='businesses'),
    path('delete/businesses/<int:business_id>', delete_business, name='delete_businesses'),
    path('logs', dboard_logs, name='logs'),
    path('404', custom_404_view, name='custom_404'),
    path('dashboard/content', content, name='content'),
    path('dashboard/content_edit', edit_content, name='edit_content'),
    path('dashboard/content_slider_images', sliderImagesList, name='sliderImagesList'),
    path('dashboard/atualizar_ordem/', atualizar_ordem, name='atualizar_ordem'),
    path('dashboard/adicionar_imagem/', adicionar_imagem, name='adicionar_imagem'),
    path('dashboard/excluir_imagemexcluir_imagem/<int:imagem_id>', excluir_imagem, name='excluir_imagem'),

    # Change Password
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='ColinaDoSol/Dashboard/Users/change-password.html',
        success_url='/'), name='change_password'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy("ColinaDoSol:password_reset_done"),
        template_name="ColinaDoSol/PasswordManagement/password_reset.html",
        email_template_name='ColinaDoSol/PasswordManagement/password_reset_email.html'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='ColinaDoSol/PasswordManagement/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy("ColinaDoSol:password_reset_complete"),
        template_name='ColinaDoSol/PasswordManagement/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='ColinaDoSol/PasswordManagement/password_reset_complete.html'
    ), name='password_reset_complete'),
]

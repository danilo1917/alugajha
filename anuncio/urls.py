from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ver_imovel, BuscaList, AnuncioCreate
from .views import (
    AnuncioUpdate,
    AnuncioDelete,
    AnuncioList,
    MeusAnunciosList,
    ContaCreate,
)

urlpatterns = [
    path("", AnuncioList.as_view(), name="index"),
    path("<int:id>/", ver_imovel, name="imovel"),
    path("buscar/", BuscaList.as_view(), name="busca"),
    path("cadastrar_anuncio", AnuncioCreate.as_view(), name="cadastrar_anuncio"),
    path("conta/criar_conta", ContaCreate.as_view(), name="criar_conta"),
    path("conta/login", LoginView.as_view(), name="login"),
    path("meus-anuncios/", MeusAnunciosList.as_view(), name="meus_anuncios"),
    path("meus-anuncios/<int:pk>", AnuncioUpdate.as_view(), name="editar_anuncio"),
    path(
        "meus-anuncios/excluir/<int:pk>",
        AnuncioDelete.as_view(),
        name="excluir_anuncio",
    ),
    path("conta/logout", LogoutView.as_view(), name="logout"),
]

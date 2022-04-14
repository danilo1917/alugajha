from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ver_imovel, busca, AnuncioCreate
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
    path("buscar/", busca, name="busca"),
    path("cadastrar_anuncio", AnuncioCreate.as_view(), name="cadastrar_anuncio"),
    path("conta/criar_conta", ContaCreate.as_view(), name="criar_conta"),
    path("conta/login", LoginView.as_view(), name="login"),
    path("meus_anuncios/", MeusAnunciosList.as_view(), name="meus_anuncios"),
    path("meus_anuncios/<int:pk>", AnuncioUpdate.as_view(), name="editar_anuncio"),
    path(
        "meus_anuncios/excluir/<int:pk>",
        AnuncioDelete.as_view(),
        name="excluir_anuncio",
    ),
    path("conta/logout", LogoutView.as_view(), name="logout"),
]

from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Anuncio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView


# Create your views here.


def ver_imovel(request, id):
    imovel = Anuncio.objects.get(pk = id)
    imovel_dict = {'imovel': {'id':imovel.id,'foto':imovel.foto,'localizacao':imovel.localizacao, 'preco':imovel.preco, 'locador':imovel.locador, 'data_post':imovel.data_post, 'alugado':imovel.alugado, 'titulo':imovel.titulo, 'telefone':imovel.telefone }}
    return render(request, 'anuncio/imovel.html', imovel_dict)


def busca(request):
    busca = request.GET.get('termo')
    resultados = Anuncio.objects.all().filter(titulo__icontains = busca).values()
    resultados = [[resultados[i]['id'], resultados[i]] for i in range(len(resultados))]
    resultados = dict(resultados)
    resultados = {"resultados":resultados}
    return render(request, 'anuncio/buscar.html', context=resultados)


def login_usr(request):
    anuncios = Anuncio.objects.all().values()
    anuncios = [[anuncios[i]['id'], anuncios[i]] for i in range(len(anuncios))]
    anuncios = dict(anuncios)
    
    anuncios = {"anuncios":anuncios}
    mensagem = ""
    if request.method =="POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username = email, password = senha)
        print(email, senha, usuario)
        if usuario is not None:
            mensagem = 'Usuário logado com sucesso!'
            login(request, usuario)
            return render(request, 'anuncio/index.html', anuncios)
        else:
            mensagem = "Usuário não existe, por favor crie uma conta e tente novamente"
    contexto = {"mensagem":mensagem}
    return render(request, 'registration/login.html', contexto)


class ContaCreate(CreateView):
    model = User
    fields = ["first_name", "last_name", "email", "password"]
    template_name = "registration/criar_conta.html"
    success_url = reverse_lazy('login')

    def get_success_url(self) -> str:
        return 'login'
   
    def form_valid(self, form) :
        User.objects.create_user(email = self.request.POST.get("email"), username = self.request.POST.get("email"), password = self.request.POST.get("password"))
        return HttpResponseRedirect(self.get_success_url())

class AnuncioCreate(CreateView):
    model = Anuncio
    fields = ["foto", "localizacao", "preco","locador","titulo","telefone"]
    template_name = 'anuncio/cadastrar_anuncio.html'
    
    def get_success_url(self):
        success_url = reverse_lazy('index')
        return success_url

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class AnuncioUpdate(UpdateView):
    model = Anuncio
    fields =  ["foto", "localizacao", "preco","locador","titulo","telefone"]
    template_name = "anuncio/atualizar_anuncio.html"
    success_url = reverse_lazy("meus_anuncios")

class AnuncioDelete(DeleteView):
    model = Anuncio
    template_name = "anuncio/deletar_anuncio.html"
    success_url = reverse_lazy("meus_anuncios")

class AnuncioList(ListView):
    model = Anuncio
    template_name = "anuncio/index.html"

class MeusAnunciosList(ListView):
    model = Anuncio
    template_name = "anuncio/meus_anuncios.html"
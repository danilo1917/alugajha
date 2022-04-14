from distutils.command.upload import upload
from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class Anuncio(models.Model):
    titulo = models.CharField(max_length=150)
    foto = models.ImageField()
    localizacao = models.CharField(max_length=200)
    preco = models.FloatField()
    locador = models.CharField(max_length=50)
    data_post = models.DateField(auto_now=True)
    alugado = models.BooleanField(default=False)
    telefone = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Generated by Django 4.0.1 on 2022-01-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("anuncio", "0002_alter_anuncio_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anuncio",
            name="foto",
            field=models.ImageField(upload_to="static/"),
        ),
    ]

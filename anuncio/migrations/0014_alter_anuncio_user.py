# Generated by Django 4.0.1 on 2022-01-20 20:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("anuncio", "0013_alter_anuncio_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anuncio",
            name="user",
            field=models.ForeignKey(
                default=django.contrib.auth.models.AbstractUser.email_user,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

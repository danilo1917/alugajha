# Generated by Django 4.0.1 on 2022-01-20 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anuncio', '0015_alter_anuncio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='user',
            field=models.ForeignKey(default='<property object at 0x000001D5EE959440>', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
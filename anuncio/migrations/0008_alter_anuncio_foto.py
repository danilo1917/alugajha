# Generated by Django 4.0.1 on 2022-01-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0007_alter_anuncio_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='foto',
            field=models.ImageField(default='media/images/apto1.jpg', upload_to='images/'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_fotosservico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='fotoPrincipal',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]

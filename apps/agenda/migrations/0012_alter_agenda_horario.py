# Generated by Django 4.2.1 on 2023-05-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_remove_oferece_profissional_remove_oferece_servico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.DateTimeField(unique=True),
        ),
    ]

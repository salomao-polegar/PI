# Generated by Django 4.2.1 on 2023-05-12 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_alter_agenda_profissional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='profissional',
        ),
    ]
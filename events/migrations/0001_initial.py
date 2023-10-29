# Generated by Django 4.2.6 on 2023-10-29 01:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nome', max_length=200)),
                ('description', models.TextField(help_text='Descrição')),
                ('url', models.URLField(help_text='URL')),
                ('date', models.DateField(help_text='Data')),
                ('time', models.TimeField(help_text='Hora')),
                ('state', models.CharField(help_text='Estado', max_length=50)),
                ('city', models.CharField(help_text='Cidade', max_length=50)),
                ('neighborhood', models.CharField(help_text='Bairro', max_length=50)),
                ('street', models.CharField(help_text='Rua', max_length=50)),
                ('number', models.IntegerField(help_text='Número do endereço')),
            ],
        ),
    ]

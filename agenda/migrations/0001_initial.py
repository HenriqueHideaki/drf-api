# Generated by Django 4.0.2 on 2023-03-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateTimeField()),
                ('nome_cliente', models.CharField(max_length=255)),
                ('email_cliente', models.CharField(max_length=255)),
                ('telefone_cliente', models.CharField(max_length=255)),
            ],
        ),
    ]

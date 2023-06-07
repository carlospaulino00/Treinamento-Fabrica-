# Generated by Django 4.2.2 on 2023-06-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostoAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('combustivel', models.CharField(max_length=50)),
                ('quantidade', models.FloatField()),
                ('valorPago', models.FloatField()),
            ],
        ),
    ]
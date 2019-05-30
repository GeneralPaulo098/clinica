# Generated by Django 2.2 on 2019-05-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('sexo', models.CharField(max_length=1)),
            ],
        ),
    ]
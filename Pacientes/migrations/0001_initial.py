# Generated by Django 4.2 on 2023-04-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=35)),
                ('apellido', models.CharField(max_length=35)),
                ('edad', models.CharField(max_length=2)),
            ],
        ),
    ]
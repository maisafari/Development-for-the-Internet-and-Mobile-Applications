# Generated by Django 4.2.7 on 2024-04-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0006_alter_administrador_votos_alter_aluno_votos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='limite',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]

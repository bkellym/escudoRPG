# Generated by Django 3.0.6 on 2020-05-27 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personagem_vampiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('natureza', models.CharField(blank=True, max_length=150, null=True)),
                ('comportamento', models.CharField(blank=True, max_length=150, null=True)),
                ('cla', models.CharField(blank=True, max_length=100, null=True)),
                ('ocupacao', models.CharField(blank=True, max_length=100, null=True)),
                ('senhor', models.CharField(blank=True, max_length=150, null=True)),
                ('conceito', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ficha_vampiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forca', models.IntegerField(blank=True, null=True)),
                ('destreza', models.IntegerField(blank=True, null=True)),
                ('vigor', models.IntegerField(blank=True, null=True)),
                ('carisma', models.IntegerField(blank=True, null=True)),
                ('manipulacao', models.IntegerField(blank=True, null=True)),
                ('aparencia', models.IntegerField(blank=True, null=True)),
                ('percepcao', models.IntegerField(blank=True, null=True)),
                ('inteligencia', models.IntegerField(blank=True, null=True)),
                ('raciocinio', models.IntegerField(blank=True, null=True)),
                ('prontidao', models.IntegerField(blank=True, null=True)),
                ('esportes', models.IntegerField(blank=True, null=True)),
                ('briga', models.IntegerField(blank=True, null=True)),
                ('esquiva', models.IntegerField(blank=True, null=True)),
                ('empatia', models.IntegerField(blank=True, null=True)),
                ('expressao', models.IntegerField(blank=True, null=True)),
                ('intimidacao', models.IntegerField(blank=True, null=True)),
                ('lideranca', models.IntegerField(blank=True, null=True)),
                ('manha', models.IntegerField(blank=True, null=True)),
                ('empatia_animais', models.IntegerField(blank=True, null=True)),
                ('oficios', models.IntegerField(blank=True, null=True)),
                ('conducao', models.IntegerField(blank=True, null=True)),
                ('etiqueta', models.IntegerField(blank=True, null=True)),
                ('armas_fogo', models.IntegerField(blank=True, null=True)),
                ('armas_branca', models.IntegerField(blank=True, null=True)),
                ('performance', models.IntegerField(blank=True, null=True)),
                ('seguranca', models.IntegerField(blank=True, null=True)),
                ('furtividade', models.IntegerField(blank=True, null=True)),
                ('sobrevivencia', models.IntegerField(blank=True, null=True)),
                ('academicos', models.IntegerField(blank=True, null=True)),
                ('computador', models.IntegerField(blank=True, null=True)),
                ('financas', models.IntegerField(blank=True, null=True)),
                ('investigacao', models.IntegerField(blank=True, null=True)),
                ('direito', models.IntegerField(blank=True, null=True)),
                ('linguistica', models.IntegerField(blank=True, null=True)),
                ('medicina', models.IntegerField(blank=True, null=True)),
                ('ocultismo', models.IntegerField(blank=True, null=True)),
                ('politico', models.IntegerField(blank=True, null=True)),
                ('ciencia', models.IntegerField(blank=True, null=True)),
                ('defesa', models.IntegerField(blank=True, null=True)),
                ('iniciativa', models.IntegerField(blank=True, null=True)),
                ('deslocamento', models.IntegerField(blank=True, null=True)),
                ('consciencia', models.IntegerField(blank=True, null=True)),
                ('autocontrole', models.IntegerField(blank=True, null=True)),
                ('coragem', models.IntegerField(blank=True, null=True)),
                ('humanidade', models.IntegerField(blank=True, null=True)),
                ('forca_vontade', models.IntegerField(blank=True, null=True)),
                ('forca_vontade_max', models.IntegerField(blank=True, null=True)),
                ('pontos_sangue', models.IntegerField(blank=True, null=True)),
                ('pontos_sangue_max', models.IntegerField(blank=True, null=True)),
                ('vitalidade', models.IntegerField(blank=True, null=True)),
                ('vitalidade_max', models.IntegerField(blank=True, null=True)),
                ('disciplina_1', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_1', models.IntegerField(blank=True, null=True)),
                ('disciplina_2', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_2', models.IntegerField(blank=True, null=True)),
                ('disciplina_3', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_3', models.IntegerField(blank=True, null=True)),
                ('disciplina_4', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_4', models.IntegerField(blank=True, null=True)),
                ('disciplina_5', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_5', models.IntegerField(blank=True, null=True)),
                ('disciplina_6', models.CharField(blank=True, max_length=150, null=True)),
                ('disciplina_valor_6', models.IntegerField(blank=True, null=True)),
                ('antecendentes_1', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_1', models.IntegerField(blank=True, null=True)),
                ('antecendentes_2', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_2', models.IntegerField(blank=True, null=True)),
                ('antecendentes_3', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_3', models.IntegerField(blank=True, null=True)),
                ('antecendentes_4', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_4', models.IntegerField(blank=True, null=True)),
                ('antecendentes_5', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_5', models.IntegerField(blank=True, null=True)),
                ('antecendentes_6', models.CharField(blank=True, max_length=150, null=True)),
                ('antecendentes_valor_6', models.IntegerField(blank=True, null=True)),
                ('qualidade_1', models.CharField(blank=True, max_length=150, null=True)),
                ('qualidade_2', models.CharField(blank=True, max_length=150, null=True)),
                ('qualidade_3', models.CharField(blank=True, max_length=150, null=True)),
                ('qualidade_4', models.CharField(blank=True, max_length=150, null=True)),
                ('qualidade_5', models.CharField(blank=True, max_length=150, null=True)),
                ('qualidade_6', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_1', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_2', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_3', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_4', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_5', models.CharField(blank=True, max_length=150, null=True)),
                ('defeito_6', models.CharField(blank=True, max_length=150, null=True)),
                ('id_personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personagem_vampiro')),
            ],
        ),
    ]

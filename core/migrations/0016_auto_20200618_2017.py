# Generated by Django 3.0.7 on 2020-06-18 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_ficha_dano_agravado'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ficha',
            new_name='Ficha_Vampiro',
        ),
        migrations.AlterModelOptions(
            name='personagem',
            options={'ordering': ['nome'], 'verbose_name': 'personagem', 'verbose_name_plural': 'personagens'},
        ),
    ]

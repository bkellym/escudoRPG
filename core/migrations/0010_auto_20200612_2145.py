# Generated by Django 3.0.7 on 2020-06-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200612_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilidade_cthulhu',
            name='coluna',
        ),
        migrations.AlterField(
            model_name='mesa',
            name='sistema',
            field=models.IntegerField(choices=[(1, 'Vampiro'), (2, 'Cthulhu')]),
        ),
    ]

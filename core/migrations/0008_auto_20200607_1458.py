# Generated by Django 3.0.7 on 2020-06-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200607_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidade_cthulhu',
            old_name='valor',
            new_name='normal',
        ),
        migrations.AddField(
            model_name='habilidade_cthulhu',
            name='bom',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='habilidade_cthulhu',
            name='extremo',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
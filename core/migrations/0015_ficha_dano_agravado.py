# Generated by Django 3.0.7 on 2020-06-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200613_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='dano_agravado',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_restorant_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='deskripsi',
            field=models.IntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='harga',
            field=models.IntegerField(null=True),
        ),
    ]
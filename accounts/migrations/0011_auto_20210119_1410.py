# Generated by Django 3.1.5 on 2021-01-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210119_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='deskripsi',
            field=models.TextField(null=True),
        ),
    ]

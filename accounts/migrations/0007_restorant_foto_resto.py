# Generated by Django 3.1.5 on 2021-01-13 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210113_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='restorant',
            name='foto_resto',
            field=models.ImageField(default='default.jpg', upload_to='documents/'),
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_menu', models.CharField(max_length=50, null=True)),
                ('harga', models.FloatField(max_length=50, null=True)),
                ('deskripsi', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='restorant',
            old_name='namaresto',
            new_name='nama_resto',
        ),
        migrations.AddField(
            model_name='restorant',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

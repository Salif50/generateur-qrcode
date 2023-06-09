# Generated by Django 4.1.1 on 2023-05-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptage', '0005_delete_essaie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_complet', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('taille', models.FloatField()),
                ('age', models.IntegerField()),
                ('marier', models.BooleanField(default=False)),
            ],
        ),
    ]

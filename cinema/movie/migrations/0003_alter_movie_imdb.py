# Generated by Django 4.1.5 on 2023-01-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_imdb_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.FloatField(),
        ),
    ]

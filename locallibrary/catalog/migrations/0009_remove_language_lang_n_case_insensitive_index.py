# Generated by Django 4.2.14 on 2024-07-15 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_genre_genre_n_case_insensitive_index'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='language',
            name='lang_n_case_insensitive_index',
        ),
    ]

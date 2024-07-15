# Generated by Django 4.2.14 on 2024-07-15 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_language_language_name_case_insensitive_unique_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='language',
            name='language_name_case_insensitive_unique',
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200, unique=True),
        ),
        migrations.AddIndex(
            model_name='language',
            index=models.Index(models.F('name'), name='lang_n_case_insensitive_index'),
        ),
    ]

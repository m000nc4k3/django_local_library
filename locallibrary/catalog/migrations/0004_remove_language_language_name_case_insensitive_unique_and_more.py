# Generated by Django 4.2.14 on 2024-07-15 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_genre_genre_name_case_insensitive_unique_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='language',
            name='language_name_case_insensitive_unique',
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200, unique=True),
        ),
        migrations.AddConstraint(
            model_name='language',
            constraint=models.UniqueConstraint(models.F('name'), name='language_name_case_insensitive_unique', violation_error_message='Language already exists (case insensitive match)'),
        ),
    ]

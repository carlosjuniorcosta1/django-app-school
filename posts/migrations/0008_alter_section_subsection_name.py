# Generated by Django 5.0.6 on 2024-09-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_genre_textual_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='subsection_name',
            field=models.CharField(blank=True, choices=[('literatura', 'Literatura'), ('cinema_tv', 'Cinema e TV'), ('games', 'Jogos'), ('comida', 'Comida'), ('artes', 'Artes')], max_length=50, null=True),
        ),
    ]

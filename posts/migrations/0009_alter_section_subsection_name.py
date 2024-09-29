# Generated by Django 5.0.6 on 2024-09-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_section_subsection_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='subsection_name',
            field=models.CharField(blank=True, choices=[('literatura', 'Literatura'), ('cinema_tv', 'Cinema e TV'), ('games', 'Jogos'), ('comida', 'Comida'), ('artes', 'Ilustrações')], max_length=50, null=True),
        ),
    ]

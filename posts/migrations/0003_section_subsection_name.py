# Generated by Django 5.0.6 on 2024-09-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_genre_textual_genre_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='subsection_name',
            field=models.CharField(blank=True, choices=[('literatura', 'Literatura'), ('cinema_tv', 'Cinema e TV'), ('games', 'Games')], max_length=50, null=True),
        ),
    ]
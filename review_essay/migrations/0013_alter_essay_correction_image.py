# Generated by Django 5.0.6 on 2024-11-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_essay', '0012_essay_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='correction_image',
            field=models.TextField(blank=True, null=True),
        ),
    ]

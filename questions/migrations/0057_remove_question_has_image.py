# Generated by Django 5.0.6 on 2025-01-08 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0056_remove_question_number_remove_question_spec_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='has_image',
        ),
    ]

# Generated by Django 5.0.4 on 2024-12-22 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0049_question_examining_board_question_spec_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='spec_subject',
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-17 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_answer_iscorrect_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='isCorrect',
        ),
    ]
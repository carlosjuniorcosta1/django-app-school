# Generated by Django 5.0.6 on 2024-07-17 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_answer_right_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='isCorrect',
        ),
    ]

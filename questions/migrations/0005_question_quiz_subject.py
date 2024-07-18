# Generated by Django 5.0.6 on 2024-07-16 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_remove_answer_created_remove_question_created_and_more'),
        ('quizes', '0007_quizsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz_subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizes.quizsubject'),
        ),
    ]
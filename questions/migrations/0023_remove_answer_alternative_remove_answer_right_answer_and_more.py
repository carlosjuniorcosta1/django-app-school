# Generated by Django 5.0.6 on 2024-07-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='alternative',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='right_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
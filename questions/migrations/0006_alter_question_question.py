# Generated by Django 5.0.6 on 2024-07-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_quiz_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=1501, null=True),
        ),
    ]

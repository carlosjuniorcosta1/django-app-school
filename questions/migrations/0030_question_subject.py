# Generated by Django 5.0.6 on 2024-07-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0029_rename_question_imag_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
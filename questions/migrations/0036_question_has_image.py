# Generated by Django 5.0.6 on 2024-07-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0035_question_number_alter_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='has_image',
            field=models.BooleanField(blank=True, default=0, null=True),
        ),
    ]
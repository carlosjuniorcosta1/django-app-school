# Generated by Django 5.0.6 on 2024-07-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0032_alter_question_context_alter_question_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
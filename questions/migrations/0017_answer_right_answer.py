# Generated by Django 5.0.6 on 2024-07-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_answer_alternative'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='right_answer',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
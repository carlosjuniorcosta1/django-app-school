# Generated by Django 5.0.6 on 2024-07-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_answer_iscorrect'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='alternative',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]

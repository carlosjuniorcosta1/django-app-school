# Generated by Django 5.0.6 on 2025-01-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0054_alter_question_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/'),
        ),
    ]

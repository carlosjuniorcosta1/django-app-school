# Generated by Django 5.0.6 on 2024-10-12 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_essay', '0003_alter_essaygrade_about_c1_alter_essaygrade_about_c2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essaygrade',
            name='about_c1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='about_c2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='about_c3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='about_c4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='about_c5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='c1',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='c2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='c3',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='c4',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)]),
        ),
        migrations.AlterField(
            model_name='essaygrade',
            name='c5',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)]),
        ),
    ]

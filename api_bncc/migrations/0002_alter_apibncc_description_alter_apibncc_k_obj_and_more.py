# Generated by Django 5.0.6 on 2024-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bncc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apibncc',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apibncc',
            name='k_obj',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='apibncc',
            name='skill',
            field=models.CharField(max_length=1000),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bncc', '0004_alter_apibncc_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apibncc',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
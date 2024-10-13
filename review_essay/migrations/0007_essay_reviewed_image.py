# Generated by Django 5.0.6 on 2024-10-12 22:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_essay', '0006_essay_about_c2_essay_about_c3_essay_about_c4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='reviewed_image',
            field=models.ImageField(blank=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp', 'svg'])]),
        ),
    ]
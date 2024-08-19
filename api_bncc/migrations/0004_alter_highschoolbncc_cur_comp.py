# Generated by Django 5.0.6 on 2024-08-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_bncc', '0003_remove_elementaryschoolbncc_school_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschoolbncc',
            name='cur_comp',
            field=models.CharField(blank=True, choices=[('linguagens', 'Linguagens'), ('matematica', 'Matemática'), ('lingua_portuguesa', 'Língua Portuguesa'), ('ciencias_humanas', 'Ciências Huamanas'), ('ciencias_da_natureza', 'Ciências da Natureza')], max_length=40, null=True),
        ),
    ]

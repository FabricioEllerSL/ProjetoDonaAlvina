# Generated by Django 5.0.2 on 2024-11-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_venda_data_venda_alter_venda_qtd_kgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='descricao_venda',
            field=models.TextField(default=''),
        ),
    ]

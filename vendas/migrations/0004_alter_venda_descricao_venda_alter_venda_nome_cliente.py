# Generated by Django 5.0.2 on 2024-11-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_venda_descricao_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='descricao_venda',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='nome_cliente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

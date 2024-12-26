import os
import django
from random import randint, uniform
from decimal import Decimal
from faker import Faker

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linguica_divina.settings')  # Substitua 'nome_do_projeto' pelo nome do seu projeto
django.setup()

from vendas.models import Venda  # Substitua 'app' pelo nome do seu app Django

# Criar instâncias de dados fictícios
fake = Faker('pt_BR')  # Gerador de dados fictícios em português

def populate_vendas(qtd):
    for _ in range(qtd):
        nome_cliente = fake.name() if randint(0, 1) else None
        valor_un_kg = randint(10, 100)  # Valor por kg entre R$10 e R$100
        qtd_kgs = Decimal(f"{uniform(1, 50):.2f}")  # Quantidade entre 1 e 50 kg
        descricao_venda = fake.sentence() if randint(0, 1) else None

        Venda.objects.create(
            nome_cliente=nome_cliente,
            valor_un_kg=valor_un_kg,
            qtd_kgs=qtd_kgs,
            descricao_venda=descricao_venda
        )

    print(f'{qtd} vendas foram adicionadas ao banco de dados.')

# Chamar a função para popular o banco
if __name__ == '__main__':
    quantidade = 10  # Defina o número de vendas a serem criadas
    populate_vendas(quantidade)

import os
import django
from random import randint, uniform
from decimal import Decimal
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linguica_divina.settings')
django.setup()

from vendas.models import Venda

fake = Faker('pt_BR')

def populate_vendas(qtd):
    counter = 0
    is_pix = 'Dinheiro'
    for _ in range(qtd):
        nome_cliente = fake.name() if randint(0, 1) else None
        valor_un_kg = randint(10, 100)
        qtd_kgs = Decimal(f"{uniform(1, 50):.2f}")
        descricao_venda = fake.sentence() if randint(0, 1) else None
        metodo_pagamento = is_pix

        is_pix = 'Pix' if is_pix != "Pix" else 'Dinheiro'


        Venda.objects.create(
            nome_cliente=nome_cliente,
            valor_un_kg=valor_un_kg,
            qtd_kgs=qtd_kgs,
            descricao_venda=descricao_venda,
            metodo_pagamento=metodo_pagamento
        )

    print(f'{qtd} vendas foram adicionadas ao banco de dados.')


if __name__ == '__main__':
    quantidade = 10
    populate_vendas(quantidade)

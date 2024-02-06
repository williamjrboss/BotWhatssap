import pandas as pd
from faker import Faker

# Função para gerar dados aleatórios
def gerar_dados(num_registros):
    fake = Faker('pt_BR')
    dados = []

    for _ in range(num_registros):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        nome_completo = f"{nome} {sobrenome}"
        telefone = fake.phone_number()
        local = fake.random_element(elements=('PE', 'PE', 'PE', 'BA', 'BA', 'CE', 'CE', 'PB', 'PB'))
        dados.append([nome_completo, telefone, local])

    return dados

# Gerar dados aleatórios
num_registros = 800
dados = gerar_dados(num_registros)

# Criar DataFrame
df = pd.DataFrame(dados, columns=['Nome Completo', 'Telefone Celular', 'Local'])

# Salvar DataFrame como planilha Excel
df.to_excel('dados_aleatorios.xlsx', index=False, engine='openpyxl')
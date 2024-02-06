import pandas as pd 
import openpyxl
import numpy as nb
from urllib.parse import quote
import webbrowser
from time import sleep 

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

dados = pd.read_excel('dados_aleatorios.xlsx')

workbook = openpyxl.load_workbook(dados)
pagina_cliente = workbook['Sheet1']

for linha in pagina_cliente.iter_rows(min_rows=2):

    nome = linha[0].value
    telefone = linha[1].value
    estado = linha[2].value
    
    mensagem  = f'Olá, Sou William estou aqui para apresentar meu trabalho como Analista de dados trazendo resultados e acompanhamentoss para todos os seu negocios, você esta interessa do nos meus serviços? so clickar no link https://wwww.portifolio.com'

    link_mensagem_whatsap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsap)
    input('')
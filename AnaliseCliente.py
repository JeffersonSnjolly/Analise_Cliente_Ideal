import pandas as pd
import plotly.express as px

tabela = pd.read_csv('clientes.csv', encoding='latin', sep=';')
tabela = tabela.drop('Unnamed: 8', axis=1)
print(tabela.info())

tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce')
print(tabela.info())

tabela = tabela.dropna()
print(tabela.info())

print(tabela.describe())

for coluna in tabela.columns:
    if (coluna != 'ClienteID' and coluna != 'Nota (1-100)'):
        grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)', text_auto=True, histfunc='avg', nbins=16)
        grafico.show()

"""
Perfil Ideal de clientes 
 * Origem: Promocões tem uma leve margem menor a compras normais   
 * Idade: Acima de 15 anos.
 * Salario: Média salarial não impacta na nota do cliente.
 * Profissôes: Entreterimento ou Artistas compram mais, (evitar clientes de construção).
 * Experiência de Trabalho: Entre dez a quinze anos de experiência.
 * Tamanho Familia: Até 7 pessoas.

"""
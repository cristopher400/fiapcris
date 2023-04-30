import pandas as pd

import seaborn as sns
from PIL._imaging import display

tabela_vendas_2019 = pd.read_csv("vendas_linha_petshop_2019.csv", encoding="ISO-8859-1", sep=";")

tabela_vendas_2020 = pd.read_csv("vendas_linha_petshop_2020.csv", encoding="ISO-8859-1", sep=";")
tabela_vendas_2021 = pd.read_csv("vendas_linha_petshop_2021.csv", encoding="ISO-8859-1", sep=";")
tabela_vendas_2022 = pd.read_csv("vendas_linha_petshop_2022.csv", encoding="ISO-8859-1", sep=";")

tabela_vendas = pd.concat([tabela_vendas_2019, tabela_vendas_2020, tabela_vendas_2021, tabela_vendas_2022])

tabela_vendas.head()

tabela_vendas['valor_total_bruto'] = tabela_vendas['valor_total_bruto'].str.replace(',', '.').astype(float)

tabela_vendas.info()

descricao = tabela_vendas['valor_total_bruto'].describe().apply(lambda x: '{:.2f}'.format(x))

print(descricao)

qtd_nulos = tabela_vendas['valor_total_bruto'].isnull().sum()

print(qtd_nulos)

tabela_vendas['valor_total_bruto'] = tabela_vendas['valor_total_bruto'].fillna(0)

print(qtd_nulos)

tabela_vendas.describe()

tabela_vendas.info()

descricao = tabela_vendas['valor_total_bruto'].describe().apply(lambda x: '{:.2f}'.format(x))

print(descricao)

sns.histplot(tabela_vendas, x="valor_total_bruto")

# Importar as bibliotecas necessárias para a limpeza dos dados
import pandas as pd
import os

path = "E:\Documentos\IT\Repositório\webscraping with python\webscraping\webscraping\dados_2023-10-27.csv"
output_path = 'cleaned_data'

# Criando uma pasta para salvar os dados limpos
try:
    os.mkdir(f'./{output_path}')
except OSError as error:
    print(error)

# Importar a planilha com os dados scrapados
data = pd.read_csv(path)

# Verificar qual o tipo de dado de cada coluna do DataFrame
print(data.dtypes)

# Retirar o símbolo 'R$' das colunas de preço à vista
data['preço à vista'] = data['preço à vista'].str.strip('R$')

# Retirar o símbolo 'R$' das colunas de preço à prazo
data['preço à prazo'] = data['preço à prazo'].str.strip('R$')

# Transformar as colunas contendo preços para float
data['preço à vista'] = data['preço à vista'].astype('float64')
data['preço à prazo'] = data['preço à prazo'].astype('float64')

print(data.info())

# Renomeando colunas para manter um padrão
data.rename(columns={'preço à vista': 'preco_a_vista', 'preço à prazo': 'preco_a_prazo'})

print(data.head())

# Salvar os dados limpos num arquivo .csv
data.to_csv(f'.\{output_path}\dados_2023-10-27.csv')
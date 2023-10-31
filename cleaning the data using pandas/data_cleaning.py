# Importar as bibliotecas necessárias para a limpeza dos dados
import pandas as pd

# Importar a planilha com os dados scrapados
data = pd.read_csv("E:\Documentos\IT\Repositório\dados.csv")

# Verificar qual o tipo de dado de cada coluna do DataFrame
print(data.info())
print(data.dtypes)

# Retirar o símbolo 'R$' das colunas de preço à vista
data['preço à vista'] = data['preço à vista'].str.strip('R$')

# Retirar o símbolo 'R$' das colunas de preço à prazo
data['preço à prazo'] = data['preço à prazo'].str.strip('R$')

print(data.head())
# Transformar as colunas contendo preços para float
data['preço à vista'] = data['preço à vista'].astype('float')
data['preço à prazo'] = data['preço à prazo'].astype('float')

# Verificando se a transformação foi bem sucedida
print("Verificando se as colunas se transformaram em float")
assert data['preço à vista'].dtype == 'float'
assert data['preço à prazo'].dtype == 'float'

# Salvar os dados limpos num arquivo .csv 
import pandas as pd
import numpy as np

# Passo 1: Ler o conteúdo do CSV com separador correto
df = pd.read_csv('arquivocopy.csv', sep=';', na_values='NaN')

# Passo 2: Exibir as informações gerais sobre o conjunto de dados
print("Informações gerais sobre o conjunto de dados:")
print(df.info())

# Verificar se as colunas foram corretamente lidas
print("\nNomes das colunas:")
print(df.columns)

# Verificar as primeiras linhas do DataFrame
print("\nPrimeiras N linhas do arquivo:")
print(df.head())

# Verificar as últimas linhas do DataFrame
print("\nÚltimas N linhas do arquivo:")
print(df.tail())

# Passo 3: Criar uma nova variável com uma cópia dos dados
df_copy = df.copy()

# Passo 4: Substituir valores nulos na coluna 'Calories' por 0
df_copy['Calories'].fillna(0, inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Calories' por 0:")
print(df_copy)

# Passo 5: Substituir valores nulos na coluna 'Date' por '1900/01/01'
df_copy['Date'].fillna('1900/01/01', inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Date' por '1900/01/01':")
print(df_copy)

# Passo 6: Transformar os dados da coluna 'Date' em datetime
df_copy['Date'] = pd.to_datetime(df_copy['Date'], errors='coerce')

# Passo 7: Verificando erros
print("\nConjunto de dados após transformação da coluna 'Date' para datetime:")
print(df_copy)

# Passo 8: Remover registros contendo valores nulos
df_copy.dropna(inplace=True)

# Passo 9: Verificar o resultado final
print("\nConjunto de dados após remover registros com valores nulos:")
print(df_copy)

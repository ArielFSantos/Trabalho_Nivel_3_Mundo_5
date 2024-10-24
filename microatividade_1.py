import pandas as pd
import numpy as np

df = pd.read_csv('arquivocopy.csv', sep=';', na_values='NaN')

print("Informações gerais sobre o conjunto de dados:")
print(df.info())

print("\nNomes das colunas:")
print(df.columns)

print("\nPrimeiras linhas do arquivo:")
print(df.head())

print("\nÚltimas linhas do arquivo:")
print(df.tail())

df_copy = df.copy()

df_copy['Calories'].fillna(0, inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Calories' por 0:")
print(df_copy)

df_copy['Date'].fillna('1900/01/01', inplace=True)
print("\nConjunto de dados após substituir valores nulos em 'Date' por '1900/01/01':")
print(df_copy)

df_copy['Date'] = pd.to_datetime(df_copy['Date'], errors='coerce')

print("\nConjunto de dados após transformação da coluna 'Date' para datetime:")
print(df_copy)

df_copy.dropna(inplace=True)

print("\nConjunto de dados após remover registros com valores nulos:")
print(df_copy)

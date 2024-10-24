import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('Arquivo.csv')  # Substitua 'arquivo.csv' pelo nome do arquivo

# Selecionar um subconjunto de colunas
subset = df[['Coluna1', 'Coluna2']]  # Substitua pelos nomes das colunas que deseja

# Selecionar linhas com base em uma condição
subset = df[df['Coluna'] > valor]  # Substitua 'Coluna' e 'valor' com os valores corretos
# Configurar o número máximo de linhas exibidas
pd.set_option('display.max_rows', 10)  # Aqui, 10 é o número máximo de linhas
# Exibir as primeiras 5 linhas
df.head(5)  # Substitua 5 pelo número de linhas que deseja visualizar
# Informações gerais sobre o DataFrame
df.info()
# Estatísticas descritivas do DataFrame
df.describe()

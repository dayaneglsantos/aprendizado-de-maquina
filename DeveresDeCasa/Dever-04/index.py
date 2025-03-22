import pandas as pd

# Caminho do arquivo
file_path = "frutas.txt"

# Lendo o arquivo e carregando os dados no DataFrame
# sep - separador
# header - está informando que não há título das colunas
# names - inclui manualmente os nomes das colunas
# engine - mecanismo de leitura (não entendi muito bem)
df = pd.read_csv(
    file_path, sep=": ", header=None, names=["Fruta", "Quantidade"], engine="python"
)

# Convertendo a coluna de quantidade para inteiro
df["Quantidade"] = df["Quantidade"].astype(int)

# Somando as quantidades das frutas repetidas
# as_index - Mantém a coluna "Fruta" como uma coluna normal em vez de transformá-la em índice do DataFrame.
df = df.groupby("Fruta", as_index=False).sum()

# Exibindo o DataFrame
print(df)

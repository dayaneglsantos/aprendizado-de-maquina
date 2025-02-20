import pandas as pd

# Lendo o arquivo csv
df = pd.read_csv('./data.csv')

selectedPosition = input('Digite a posição do usuário que deseja ver as informações: ')
registro = int(selectedPosition) - 1

# Verifica se o registro digitado é válido
if registro < 0 or registro >= len(df):
    print('Registro inválido ou não encontrado')
    exit()

# Pega a linha correspondente ao valor digitado
linha = df.iloc[registro]

# Transforma as datas para o formato dd/mm/aaaa
dataNascimento = pd.to_datetime(linha['dataNascimento']).strftime('%d/%m/%Y')
dataCadastro = pd.to_datetime(linha['dataCadastro']).strftime('%d/%m/%Y')

resultado = (
        f"Registro {registro + 1}: "
        f"Nome: {linha['nome']}, "
        f"Data de nascimento: {dataNascimento}, "
        f"Data de registro: {dataCadastro}, "
        f"Horário de cadastro: {linha['horaCadastro']}"
    )
    
print(resultado)


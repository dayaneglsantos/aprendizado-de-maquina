import csv

lista = []
with open("./dados.csv") as csvfile:
    file = csv.reader(csvfile)
    next(file)  # Usado para ignorar o cabeçalho
    for row in file:
        lista.append(row)

nomeDigitado = input('Digite o nome a ser pesquisado: ')
nomeDigitado = nomeDigitado.lower()

# Encontra a pessoa mais velha na lista
maisVelho = max(lista, key=lambda row: int(row[1]))

# Verifica se o nome digitado está na lista
encontrado = any(row[0].lower() == nomeDigitado for row in lista)

# Se encontrado, verifica se é a pessoa mais velha
if encontrado:
    # Obter a pessoa com o nome digitado
    encontrado = next(row for row in lista if row[0].lower() == nomeDigitado)
    idadePessoaDigitada = int(encontrado[1])

    if encontrado == maisVelho:
        print(f'{encontrado[0]} é a pessoa mais velha da lista!')
    else:
        print(f'{encontrado[0]} não é a pessoa mais velha.')
else:
    print("Nome não encontrado.")

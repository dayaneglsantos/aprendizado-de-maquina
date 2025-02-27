userString = input("Digite uma frase: ")
# separa a string em uma lista
splitedString = userString.split()
# verifica de a lista possui mais de 1 item
validString = len(splitedString) > 1

# verifica se a string foi digitada e se possui pelo menos 2 palavras
if len(userString) == 0 or not validString:
    print("Você deve digitar uma frase com pelo menos 2 palavras" )
    exit()

print (f"A frase digitada possui {len(userString)} caracteres")
print (f"A frase digitada possui {len(splitedString)} palavras")
print (f"A maior palavra digitada foi {max(splitedString, key=len)}")
print(f"A frase invertida fica: {userString[::-1]}")


print(f"A frase com uppercase fica: {userString.upper()}")
print(f"A frase com lowercase fica: {userString.lower()}")
print(f"A listagem das palavras em tupla é: {tuple(splitedString)}")

# Inverte cada palavra na lista
invertedWords = [palavra[::-1] for palavra in splitedString]
print(f"A listagem das palavras invertidas fica: {invertedWords}")

# Junta as palavras invertidas de volta em uma frase
invertedString = " ".join(invertedWords)
print(f"A frase com as palavras invertidas fica: {invertedString}")


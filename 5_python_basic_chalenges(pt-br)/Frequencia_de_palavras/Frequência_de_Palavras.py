from collections import Counter

def frequencia(texto):
    lowercase = texto.lower()
    resultado = ""
    for char in lowercase:
        if char.isalnum() or char.isspace():  # só letras/números ou espaço
            resultado += char
    lista = resultado.split()
    dicionario = Counter(lista)
    return dicionario

texto = input("Insira um texto: ")
print(frequencia(texto))


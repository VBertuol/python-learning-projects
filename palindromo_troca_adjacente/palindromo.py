# resolução O(n^2)

def palindromo(string):
    if len(string) <= 1:
        return string
    
    if string == string[::-1]:
        return string
    
    for i in (range(len(string) - 1)):
        troca = string[i+1] + string[i]
        inicio = string[:i]
        fim = string[i+2:]
        resultado = inicio + troca + fim
        if resultado == resultado[::-1]:
            return resultado

    return '-1'

print(palindromo(input()))
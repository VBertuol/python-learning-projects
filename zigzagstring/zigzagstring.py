def StringChallenge(strArr):
    texto = strArr[0]
    num_linhas = int(strArr[1])
    linha = 0
    descendo = True
    lst = [""] * num_linhas
    
    if num_linhas == 1 or num_linhas >= len(texto):
        return texto    

    for char in texto:
        lst[linha] += char
        if descendo:
            linha += 1
        else:
            linha -= 1
        if linha == num_linhas - 1:
            descendo = False
        if linha == 0:
            descendo = True

    resultado = "".join(lst)
        
    return resultado


# Teste
print(StringChallenge(["coderbyte", "3"]))  # deve imprimir 'creoebtdy'
'''Linha 1: c   r   e
   Linha 2:  o e b t
   Linha 3:   d   y'''

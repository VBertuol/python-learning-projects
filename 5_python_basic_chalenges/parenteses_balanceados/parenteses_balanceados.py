def valida(entrada):
    lista = []
    for char in entrada:
        print(lista)
        if char in '({[':
            lista.append(char)
        elif char == ')':
            if lista[-1] == '(':
                lista.pop()
        elif char == '}':
            if lista[-1] == '{':
                lista.pop()
        elif char == ']':
            if lista[-1] == '[':
                lista.pop()
        else: return False

    print(lista)
    if len(lista) == 0: return True
    else: return False

entrada = input("Entrada: ")
if valida(entrada): print("Entrada válida")
else: print("Entrada inválida")
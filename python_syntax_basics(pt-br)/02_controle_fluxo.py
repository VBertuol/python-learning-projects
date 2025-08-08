# 02_controle_fluxo.py
# Guia demonstrativo de Python: Estruturas de Controle (if, loops e fluxo adicional)

# ====================================================================
# 1. Condicionais: if / elif / else
# ====================================================================

# Sintaxe básica
x = 42
if x > 0:
    # bloco executado quando a condição é verdadeira
    positivo = True
elif x == 0:
    # bloco executado quando primeira condição é falsa e esta é verdadeira
    zero = True
else:
    # bloco executado quando todas as condições acima são falsas
    negativo = True

# Expressões condicionais compostas
y = 10
if x > 0 and y > 0:
    ambos_positivos = True

# Comparações encadeadas
z = 3
if 1 < z < 5:
    dentro_intervalo = True

# Dica: evite condicionais muito profundas; extraia lógica em funções

# ====================================================================
# 2. Laço for
# ====================================================================

# Iterando sobre sequência
lista = ["a", "b", "c"]
for item in lista:
    # código que roda para cada item em lista
    pass

# Usando range(start, stop, step)
for i in range(0, 10, 2):
    # 0, 2, 4, 6, 8
    pass

# enumerate() para índice + valor
enumerados = []
for indice, valor in enumerate(lista):
    enumerados.append((indice, valor))

# zip() e unpacking
cores = ["vermelho", "verde", "azul"]
numeros = [1, 2, 3]
for cor, num in zip(cores, numeros):
    # combina dois iteráveis
    pass

# Dica: comprehensions para casos simples
# ex: quadrados = [i**2 for i in range(10)]

# ====================================================================
# 3. Laço while
# ====================================================================

# Loop com condição de saída
contador = 0
while contador < 5:
    # faz algo
    contador += 1
else:
    # executa quando condição do while se torna falsa
    terminou = True

# Dica: cuidado com loops infinitos; sempre modifique variável de controle

# ====================================================================
# 4. Controle de fluxo adicional
# ====================================================================

# break: sai do laço imediatamente
encontrado = False
for i in range(10):
    if i == 5:
        encontrado = True
        break

# continue: pula para a próxima iteração
for i in range(5):
    if i % 2 == 0:
        continue  # ignora pares
    # aqui só ímpares

# pass: placeholder sem efeito
for _ in range(3):
    pass  # TODO: implementar mais tarde

# Exemplo de laço externo + interno com flag
encontrado = False
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        if a + b == 7:
            encontrado = True
            break
    if encontrado:
        break

# Dica: else em for (executa se não houve break)
for n in range(3):
    if n == 10:
        break
else:
    # este bloco roda se nunca houve break
    nao_encontrado = True

# ====================================================================
# 5. Expressão condicional (ternário)
# ====================================================================

# sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
idade = 20
status = "Maior" if idade >= 18 else "Menor"

# ====================================================================
# 6. Dicas e armadilhas comuns
# ====================================================================

# is vs. ==
a_lista1 = [1, 2, 3]
a_lista2 = a_lista1
# a_lista1 is a_lista2 -> True (mesmo objeto)
# a_lista1 == a_lista2 -> True (mesmo conteúdo)

# Evitar modificar lista durante iteração:
# for x in lista: lista.remove(x) -> comportamento inesperado

# Legibilidade: limite de indentação (máximo ~3 níveis)
# Extraia funções para reduzir profundidade

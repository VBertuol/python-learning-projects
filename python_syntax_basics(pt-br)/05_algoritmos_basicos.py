# 05_algoritmos_basicos.py
# Guia demonstrativo de Python: Algoritmos Fundamentais – Busca, Ordenação e Recursão

# ====================================================================
# 1. Busca Linear
# ====================================================================

# Percorrer lista até encontrar elemento (Complexidade O(n))
def busca_linear(lista, alvo):
    # retorna índice ou -1 se não encontrado
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

# ====================================================================
# 2. Busca Binária
# ====================================================================

# Pré-requisito: lista ordenada
ordenada = [1, 3, 5, 7, 9]

# Implementação iterativa (O(log n))
def busca_binaria_iterativa(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# Implementação recursiva (O(log n))
def busca_binaria_recursiva(lista, alvo, esquerda=0, direita=None):
    if direita is None:
        direita = len(lista) - 1
    if esquerda > direita:
        return -1
    meio = (esquerda + direita) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita)
    else:
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1)

# ====================================================================
# 3. Conceitos de Ordenação (pseudo-código breve)
# ====================================================================

# Bubble Sort: compara pares adjacentes e troca se fora de ordem (O(n²))
# for i in range(len(lista)):
#     for j in range(0, len(lista)-i-1):
#         if lista[j] > lista[j+1]:
#             swap(lista[j], lista[j+1])

# Insertion Sort: insere cada elemento na posição correta (O(n²))
# for i in range(1, len(lista)):
#     chave = lista[i]
#     j = i-1
#     while j >= 0 and lista[j] > chave:
#         lista[j+1] = lista[j]
#         j -= 1
#     lista[j+1] = chave

# Selection Sort: seleciona o menor e troca com posição atual (O(n²))
# for i in range(len(lista)):
#     min_idx = i
#     for j in range(i+1, len(lista)):
#         if lista[j] < lista[min_idx]:
#             min_idx = j
#     swap(lista[i], lista[min_idx])

# Dica: em prática, usar sorted() ou list.sort() para eficiência

# ====================================================================
# 4. Recursão
# ====================================================================

# Estrutura: caso base + passo recursivo

# Fatorial
def fatorial(n):
    # caso base
    if n <= 1:
        return 1
    # passo recursivo
    return n * fatorial(n - 1)

# Sequência de Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Percorrer estrutura aninhada (árvore simples)
class No:
    def __init__(self, valor, filhos=None):
        self.valor = valor
        self.filhos = filhos or []


def percorrer_arvore(no):
    # caso base implícito: filhos vazios
    print(no.valor)
    for filho in no.filhos:
        percorrer_arvore(filho)

# ====================================================================
# 5. Iteração vs. Recursão
# ====================================================================

# Vantagens da iteração: menor uso de pilha de chamadas
# Vantagens da recursão: código mais conciso para problemas naturalmente recursivos

# Limite de recursão
import sys
# sys.setrecursionlimit(10000)  # aumentar limite se necessário

# ====================================================================
# 6. Dicas
# ====================================================================

# - Divida problemas recursivos em subproblemas menores
# - Use memoização ou functools.lru_cache para evitar recomputações
# - Cuidado com profundidade de recursão e estouro de pilha
# - Prefira algoritmos O(n log n) ou melhores quando possível

# 06_problemas_multietapa.py
# Guia demonstrativo de Python: Combinação de Estruturas, Otimização e Casos de Borda

# ====================================================================
# 1. Problemas compostos
# ====================================================================

# Exemplo: contar frequência + ordenar resultados
dados = ['a','b','a','c','b','a']
# Contagem de frequência usando dict
freq = {}
for x in dados:
    freq[x] = freq.get(x, 0) + 1
# Ordenar por frequência
tipos_ordenados = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)

# Exemplo: filtrar dados com condições múltiplas
numeros = list(range(20))
pares_grandes = [n for n in numeros if n % 2 == 0 and n > 10]

# ====================================================================
# 2. Análise de Complexidade (Big O)
# ====================================================================

# Notação comum: O(n), O(n log n), O(n**2)
# Exemplo comparativo:
# - Busca linear: O(n)
# - Busca binária: O(log n)
# - Sorted: O(n log n)

# ====================================================================
# 3. Tratamento de Casos de Borda
# ====================================================================

# Listas vazias, None, valores extremos
valores = []
if not valores:
    # caso de lista vazia
    pass

# Validação de entrada

def processar(lista):
    assert lista is not None, "lista não pode ser None"
    assert isinstance(lista, list), "entrada deve ser lista"
    # resto da lógica...

# ====================================================================
# 4. Técnica Greedy (Gulosa)
# ====================================================================

# Exemplo: troco mínimo com moedas fictícias
troco = 87
moedas = [50, 20, 10, 5, 1]
resultado = {}
for moeda in moedas:
    qtd = troco // moeda
    if qtd:
        resultado[moeda] = qtd
        troco %= moeda
# resultado -> {50:1,20:1,10:1,5:1,1:2}

# ====================================================================
# 5. Problemas de múltiplos passos
# ====================================================================

# Dividir em funções menores
def etapa1(dados):
    # pré-processamento
    return [d*2 for d in dados]

def etapa2(dados):
    # filtragem simples
    return [d for d in dados if d > 5]

def processo_completo(dados):
    d1 = etapa1(dados)
    d2 = etapa2(d1)
    # uso de estrutura auxiliar (fila)
    from collections import deque
    fila = deque(d2)
    return list(fila)

# ====================================================================
# 6. Otimização simples
# ====================================================================

# Memoização via dicionário
dp = {}
def fib_memo(n):
    if n in dp:
        return dp[n]
    if n <= 1:
        dp[n] = n
    else:
        dp[n] = fib_memo(n-1) + fib_memo(n-2)
    return dp[n]

# Uso de functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

# ====================================================================
# 7. Dicas Gerais
# ====================================================================

# - Escreva testes simples para cada função/etapa
# - Documente pré-condições e pós-condições
# - Valide entradas antes de processar
# - Comente o propósito de cada bloco principal

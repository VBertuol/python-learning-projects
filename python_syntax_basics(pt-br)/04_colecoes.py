# 04_colecoes.py
# Guia demonstrativo de Python: Coleções – Listas, Tuplas, Sets e Dicionários

# ====================================================================
# 1. Listas
# ====================================================================

# Criação e indexação
lista = [1, 2, 3, 4]
primeiro = lista[0]
ultimo = lista[-1]

# Métodos de listas 
lista.append(5)         # adiciona ao final
lista.extend([6, 7])    # adiciona múltiplos elementos
lista.insert(0, 0)      # insere 0 na posição 0
removido = lista.pop()  # remove e retorna o último item
lista.remove(2)         # remove a primeira ocorrência de 2
lista.sort()            # ordena a lista in-place
lista.reverse()         # inverte a lista in-place

# Slicing e cópia
sub_lista = lista[1:4]                # fatia da lista
copia_rasa = lista.copy()             # copia superficial (shallow copy)

# Cópia profunda
import copy
copia_profunda = copy.deepcopy(lista) # cópia profunda (deep copy)

# ====================================================================
# 2. Tuplas
# ====================================================================

# Sintaxe e imutabilidade
tupla = (10, 20, 30)
# tupla[0] = 5  # Erro: tuplas são imutáveis

# Desempacotamento
a, b, c = tupla  # a=10, b=20, c=30

# Uso como chave de dicionário ou elemento de set
d = {tupla: "valor associado"}

# ====================================================================
# 3. Sets
# ====================================================================

# Criação de sets
conjunto = {1, 2, 3, 2}     # duplicatas são removidas
conjunto_vazio = set()

# Operações de conjunto
uni = conjunto.union({3,4})           # {1,2,3,4}
inter = conjunto.intersection({2,3})  # {2,3}
diff = conjunto.difference({1})       # {2,3}

# Dica: usar set para remover duplicatas de lista
sem_duplicatas = list(set([1,2,2,3,3]))

# ====================================================================
# 4. Dicionários
# ====================================================================

# Criação literal e via dict()
dict_literal = {"a": 1, "b": 2}
dict_via = dict(c=3, d=4)

# Acesso e métodos
valor_a = dict_literal["a"]
valor_x = dict_literal.get("x", 0)  # retorna 0 se chave não existir
chaves = list(dict_literal.keys())
valores = list(dict_literal.values())
itens = list(dict_literal.items())

dict_literal.update({"e":5})  # adiciona/atualiza chave
dict_literal.pop("b")       # remove e retorna valor

# ====================================================================
# 5. Casos de uso avançados
# ====================================================================

# Contagem de frequência (menção ao collections.Counter)
from collections import Counter
contador = Counter(["a", "b", "a"])  # {'a': 2, 'b': 1}

# Agrupamento de dados via dicionário de listas
itens = [("categoria1", 5), ("categoria2", 3), ("categoria1", 2)]
agrupado = {}
for cat, val in itens:
    agrupado.setdefault(cat, []).append(val)
# agrupado -> {'categoria1':[5,2], 'categoria2':[3]}

# Ordenação de dicionário por valor
sorted_items = sorted(dict_literal.items(), key=lambda x: x[1])

# ====================================================================
# 6. Dicas
# ====================================================================

# - List vs Tuple: tuple é imutável e pode ser usado como chave; liste é mutável
# - Sets não mantêm ordem
# - Dict mantém inserção (Python 3.7+)
# - Use comprehensions:
#   lista_compr = [i*2 for i in range(5)]
#   set_compr = {i for i in lista if i%2==0}
#   dict_compr = {k:v for k,v in dict_literal.items() if v>1}
# - Cuidado com mutabilidade compartilhada: usar copia quando necessário

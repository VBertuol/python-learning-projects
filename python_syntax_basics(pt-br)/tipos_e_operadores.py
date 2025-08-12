  # 01_tipos_e_operadores.py
# Guia demonstrativo de Python: Tipos de Dados, Literais, Operadores e Sintaxe Básica

# ====================================================================
# 1. Declaração e uso de variáveis
# ====================================================================

# Convenção de nomes: snake_case
minha_variavel = 10
outra_variavel, terceira_variavel = 1, 2  # Atribuição múltipla

# Tipagem dinâmica x estática (Python é dinamicamente tipado)
# Em linguagens estáticas, seria: int x = 5;

# ====================================================================
# 2. Tipos primitivos e literais
# ====================================================================

# int
numero_inteiro = 42

# float
numero_float = 3.1415
numero_exponencial = 1.2e3  # float exponencial -> 1200.0

# bool
verdadeiro = True
falso = False

# str
texto_simples = 'Olá, Python!'
texto_duplas = "Strings podem usar aspas duplas"
texto_multilinha = '''
Texto em várias
linhas com aspas triplas
'''

# Literais numéricos especiais
binario = 0b1010     # 10 em decimal
hexadecimal = 0xFF    # 255 em decimal

# Conversão de tipos
s_num = "123"
int_de_str = int(s_num)       # 123
float_de_str = float(s_num)   # 123.0
str_de_int = str(456)         # "456"
bool_de_str = bool("")      # False, string vazia é falsy

# ====================================================================
# 3. Operadores aritméticos
# ====================================================================

a, b = 7, 3
soma = a + b         # 10
subtracao = a - b    # 4
produto = a * b      # 21
divisao = a / b      # 2.333...
div_inteira = a // b # 2 (divisão inteira)
resto = a % b        # 1
potencia = a ** b    # 343

# Precedência de operadores
resultado = (a + b) * 2  # parênteses alteram a precedência

# ====================================================================
# 4. Operadores de comparação e lógicos
# ====================================================================

# Comparação
igual = (a == b)        # False
diferente = (a != b)    # True
maior = (a > b)         # True

# Lógicos
cond1 = True
cond2 = False
and_result = cond1 and cond2  # False (curto-circuito: avalia o primeiro False)
or_result = cond1 or cond2    # True  (curto-circuito: retorna True sem avaliar cond2)
not_result = not cond1        # False

# Truthiness: valores considerados falsy: 0, 0.0, "", [], {}, None
# Exemplo:
if not "":
    pass  # este bloco será executado, pois "" é falsy

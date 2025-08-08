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

# ====================================================================
# 5. Manipulação básica de strings
# ====================================================================

frase = "  Python é incrível!  "

# Métodos comuns
frase_up = frase.upper()            # "  PYTHON É INCRÍVEL!  "
palavras = frase.split()            # ["Python", "é", "incrível!"]
sem_espacos = frase.strip()         # "Python é incrível!"
modificada = frase.replace("incrível", "fantástico")

# Formatação
um_valor = 3.14159
f_str = f"O valor de pi é aproximadamente {um_valor:.2f}"  # duas casas decimais
fmt_str = "O valor de pi é aproximadamente {:.2f}".format(um_valor)

# Indexação e slicing
primeiro = frase[0]     # ' '
ultimo = frase[-1]      # ' '
parte = frase[2:8]      # 'Python'[0:6] exemplo adaptado

# ====================================================================
# 6. Cálculos simples e dicas de precisão
# ====================================================================

# Ponto flutuante pode gerar surpresas:
x = 0.1 + 0.2
# x pode resultar em 0.30000000000000004

# Uso de decimal para precisão (menção rápida)
from decimal import Decimal
preciso = Decimal('0.1') + Decimal('0.2')  # => Decimal('0.3')

# ====================================================================
# 7. Dicas e boas práticas
# ====================================================================

# - Evite "variáveis mágicas" sem significado, ex: x=5 vs. contador_de_usuarios=5
# - Comente o "por quê", não o "como" quando o código já é óbvio
# - Prefira literais quando claros, ou construtores (e.g., [] vs. list()) quando quiser enfatizar tipo

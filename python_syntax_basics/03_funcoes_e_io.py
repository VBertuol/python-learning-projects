# 03_funcoes_e_io.py
# Guia demonstrativo de Python: Funções Built-in e I/O Básico

# ====================================================================
# 1. Principais funções built-in
# ====================================================================

# len(): comprimento de sequência
lista = [1, 2, 3]
tamanho = len(lista)  # 3

# type(): tipo do objeto
tipo_lista = type(lista)  # <class 'list'>

# print(): saída no console
print("Olá, mundo!", "Outro texto", sep=" - ", end="\n---\n")

# input(): lê string do usuário
# nome = input("Digite seu nome: ")

# min(), max(), sum()
valores = [5, 2, 9]
menor = min(valores)
maior = max(valores) 
nsoma_total = sum(valores)

# abs(), round()
modulo = abs(-7)
arredondado = round(3.14159, 2)  # 3.14

# sorted(): retorna nova lista ordenada
original = [3, 1, 2]
ordenada = sorted(original)  # [1, 2, 3]

# reversed(): itera na ordem inversa
for elemento in reversed(original):
    pass  # 2,1,3

# enumerate(), zip()
enum_ex = list(enumerate(['a', 'b', 'c']))  # [(0,'a'),...]
zip_ex = list(zip([1,2], ['x','y']))           # [(1,'x'),...]

# ====================================================================
# 2. Entrada de dados (I/O de console)
# ====================================================================

# input() sempre retorna str\entrada = "123"  # simulação de input("Digite um número: ")

entrada = input("Digite um número: ")
try:
    numero = int(entrada)  # converte para int
except ValueError:
    numero = None  # tratamento de exceção simples

# ====================================================================
# 3. Saída formatada
# ====================================================================

# print() com sep e end já demonstrado acima

# F-strings avançadas: alinhamento e números
valor = 7.5
# alinhado à direita com largura 10 e 2 casas decimais
fstring_ex = f"|{valor:>10.2f}|"
# alinhado à esquerda: {valor:<10.2f}

# ====================================================================
# 4. Leitura e escrita de arquivos (modo básico)
# ====================================================================

caminho = 'exemplo.txt'

# modo 'r' (leitura)
with open(caminho, 'r') as f:
    conteudo = f.read()

# modo 'w' (escrita, apaga arquivo existente)
with open(caminho, 'w') as f:
    f.write("Texto de exemplo\n")

# modo 'a' (append): adiciona ao final\ nwith open(caminho, 'a') as f:
    f.write("Outra linha\n")

# modo 'r+' (leitura + escrita)
with open(caminho, 'r+') as f:
    linhas = f.readlines()
    # posição de escrita: f.seek(0)
    f.write("Início do arquivo\n")

# Dicas:
# - Usar context manager (with) garante fechamento automático
# - Tratar exceções de I/O com try/except se necessário
# - Para arquivos grandes, iterar por linhas ao invés de f.read()

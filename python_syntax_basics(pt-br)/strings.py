string = "Olá mundo"

string[0] # = 'O', primeiro caracter
string[-1] # = 'o', último caracter
string[4:9] # = 'mundo', caracteres da posição 4 a 8
string[4:] # = 'mundo', caracteres da posição 4 até o final
string[:4] # = 'Olá', caracteres do inicio até caracter 3
string[::2] # string inteira pulando de 2 em 2
string[::-1] # string inversa

# Método capitalize()
# Primeiro caracter (string[0]) maiúsculo, resto minúsculo.
string = "olá mundo"
string.capitalize() # = "Olá mundo"

# Método center()
# Centraliza a string. Primeiro argumento é o número de caracteres total, incluindo da string inicial.
string = "olá mundo"
string.center(9) # = "olá mundo"
string.center(11) # = " olá mundo "
# Segundo argumento: caracter de preenchimento do espaço lateral.
string.center(13, '*') # = "**olá mundo**"

# Método endswith()
# Verifica se a string termina com a sub-string dada como argumento e retorna True ou False
string = "olá mundo"
string.endswith('do') # = True
string.endswith('olá') # = False

# Método startswith()
# Verifica se a string começa com a sub-string dada como argumento e retorna True ou False
string = "olá mundo"
string.endswith('do') # = False
string.endswith('olá') # = True

# Método find()
# Procura por uma substring e retorna o índice da primeira ocorrência desta substring.
string = "olá mundo"
string.find("mundo") # = 4
string.find("xyz") # = -1
# Segundo argumento: começar a procurar a partir da posição x
string.find("mundo", 3) # = 4

# Método rfind()
# Mesma coisa que find() mas começa a busca pelo fim da string
string = "olá mundo"
string.rfind("mundo") # = 4
string.rfind("xyz") # = -1

# Método isalnum()
# Verifica se a string contém apenas números ou letras e retorna True ou False
string = "olámundo"
string.isalnum() # True
string = "olámundo1"
string.isalnum() # True
string = "olá mundo"
string.isalnum() # False

# Método isalpha()
# Verifica se a string contém apenas letras e retorna True ou False
string = "olámundo"
string.isalnum() # True
string = "olámundo1"
string.isalnum() # False
string = "olá mundo"
string.isalnum() # False

# Método isdigit()
# Verifica se a string contém apenas números e retorna True ou False
string = "123"
string.isalnum() # True
string = "123 "
string.isalnum() # False

# Método islower()
# Verifica se a string contém apenas letras minúsculas e retorna True ou False
string = "olámundo"
string.isalnum() # True
string = "Olámundo"
string.isalnum() # False
string = "olá mundo"
string.isalnum() # False

# Método isspace()
# Verifica se a string contém apenas espaços em branco e retorna True ou False
string = " "
string.isspace() # True
string = "\n"
string.isspace() # True
string = "a"
string.isspace() # False
string = ""
string.isspace() # False

# Método isupper()
# Verifica se a string contém apenas letras maiúsculas e retorna True ou False
string = "OLÁMUNDO"
string.isalnum() # True
string = "Olámundo"
string.isalnum() # False
string = "OLÁ MUNDO"
string.isalnum() # False

# Método join()
# Une todas as strings de uma lista em uma única string usando a string de chamada de método como separador
string = " "
lista = ["Olá", "mundo"]
string.join(lista) # = "Olá mundo"

# Método lower()
# Substitui todas as letras maiúsculas com suas equivalentes minúsculas
string = "Olá Mundo"
string.lower() # = "olá mundo"

# Método upper()
# Substitui todas as letras minúsculas com suas equivalentes maiúsculas
string = "Olá Mundo"
string.upper() # = "OLÁ MUNDO"

# Método lstrip()
# Remove todos os espaços em branco iniciais
string = " Olá mundo "
string.lstrip() # = "Olá mundo "
# Primeiro argumento: remove todos os caracteres INICIAIS listados em seu argumento (string)
string = " Olá mundo "
string.lstrip(" O") # = "lá mundo"
string.lstrip("O") # = " Olá mundo "

# Método rstrip()
# Mesma coisa que lstrip() mas no FIM da string
string = " Olá mundo "
string.rstrip() # = " Olá mundo"
string = " Olá mundo "
string.lstrip("o ") # = " Olá mund"

# Método strip()
# Combina lstrip() com rtrip() removendo os espaços em branco iniciais e finais
string = " Olá mundo "
string.strip() # = "Olá mundo"

# Método replace()
# Com dois parâmetros, retorna uma cópia da string original em que todas as ocorrências do primeiro argumento foram substituídas pelo segundo argumento
string = "Olá mundo"
string.replace("mundo", "amigo") # = "Olá amigo"
string.replace("mundo", "") # = "Olá "
string.replace("", "a") # = "aOalaáa amauanadaoa"
# Um terceiro parametro pode limitar o número de substituições
string = "a a a"
string.replace("a", "o", 2) # = "o o a"

# Método split()
# Divide a string e cria uma lista de todas as substrings detectadas, presume que as substrings estão delimitadas por espaços em branco (inverso de join())
string = "Olá mundo"
string.split() # = ["Olá", "mundo"]
string = "Olá\nmundo"
string.split() # = ["Olá", "mundo"]

# Método swapcase()
# Cria uma nova string ao inverter as letras maiúsculas para minúsculas e vice-versa.
string = "Olá mundo"
string.swapcase() # = "oLÁ MUNDO"

# Método title()
# Primeira letra de cada palavra em maiúscula e todas as outras letras em minúsculas.
string = "olá mundo"
string.title() # = "Olá Mundo"


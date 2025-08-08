Desafio: Analisador de Frequência de Palavras

● Enunciado: Crie uma função em Python que receba uma string de texto como
entrada e retorne um dicionário. Este dicionário deve conter cada palavra única
do texto como chave e sua frequência (número de ocorrências) como valor. As
palavras devem ser tratadas de forma case-insensitive (maiúsculas e minúsculas
são consideradas a mesma palavra), e pontuações (como '.', ',', '!', '?') devem ser
ignoradas.

● Exemplos:
○ Entrada: "Olá mundo! Olá, Python."
○ Saída esperada: {'olá': 2, 'mundo': 1, 'python': 1}
○ Entrada: "A casa é azul. A casa, azul."
○ Saída esperada: {'a': 2, 'casa': 2, 'é': 1, 'azul': 2}

● Restrições: A string de entrada pode conter letras (maiúsculas e minúsculas),
números, espaços e pontuações comuns. Considerar apenas palavras separadas
por espaços ou pontuações.

● Dicas/Considerações: Pense em como normalizar as palavras (converter para
minúsculas, remover pontuações) antes de contá-las. Qual estrutura de dados é
ideal para armazenar contagens de forma eficiente e permitir buscas rápidas?
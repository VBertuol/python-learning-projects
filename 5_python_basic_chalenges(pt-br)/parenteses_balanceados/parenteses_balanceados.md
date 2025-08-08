Validador de Parênteses Balanceados

● Enunciado: Escreva uma função em Python que determine se uma string de
entrada contendo apenas os caracteres '(', ')', '{', '}', '[' e ']' é válida. Uma string é
considerada válida se:
1. Parênteses abertos devem ser fechados pelo mesmo tipo de parênteses.
2. Parênteses abertos devem ser fechados na ordem correta.
3. Toda parêntese fechado tem um parêntese aberto do mesmo tipo
correspondente.

● Exemplos:
○ Entrada: "(){}" -> Saída: True
○ Entrada: "(]" -> Saída: False
○ Entrada: "([{}])" -> Saída: True
○ Entrada: "{}" -> Saída: True
○ Entrada: ")(" -> Saída: False

● Restrições: A string conterá apenas os caracteres especificados. A string pode
ser vazia.

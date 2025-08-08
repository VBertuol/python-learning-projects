def encontrar_par_soma_alvo(nums, alvo):
    vistos = {}

    for i, num in enumerate(nums):
        complemento = alvo - num
        if complemento in vistos:
            return f'{[vistos[complemento], i]} ({complemento} + {num})'
        vistos[num] = i

    return 'Não encontrado'

# ========================
# Casos de teste
# ========================
print(encontrar_par_soma_alvo([2, 7, 11, 15], 9))   # Esperado: [0, 1] (2 + 7)
print(encontrar_par_soma_alvo([3, 2, 4], 6))        # Esperado: [1, 2] (2 + 4)
print(encontrar_par_soma_alvo([3, 3], 6))           # Esperado: [0, 1] (3 + 3)

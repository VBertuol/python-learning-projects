def maior_soma_subarray(nums):
    soma_atual = nums[0]
    maior_soma = nums[0]

    for num in nums[1:]:
        # Escolher entre continuar ou recomeçar
        soma_atual = max(num, soma_atual + num)
        # Atualizar a melhor soma
        maior_soma = max(maior_soma, soma_atual)

    return maior_soma



# ========================
# Casos de teste
# ========================
print(maior_soma_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Esperado: 6
print(maior_soma_subarray([1]))                              # Esperado: 1
print(maior_soma_subarray([5, 4, -1, 7, 8]))                  # Esperado: 23
print(maior_soma_subarray([-1, -2, -3]))                      # Esperado: -1

#questão 01
valores = [int(input("Informe uma lista de números inteiros, com pelo menos 4 valores:"))]
print(f"Lista original: {valores}.")

print("Lista dos 3 primeiros elementos:", valores[:3])

print("Lista dos 2 últimos elementos:", valores[1:])#

print("Lista invertida:", reverse(valores))

print("Lista dos elementos de índice par:", valores[::2])

indices_impares = []
for indice in range(len(valores)):
    if (indice/2) != 0:
        indices_impares.append()
    print(f"Lista dos elementos de índice ímpar: {indices_impares}.")

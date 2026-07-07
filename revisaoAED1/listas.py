#questão 01 ____ERRO
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

#Questão 02 ____ERRO

while True:
    resposta = int(input("Deseja informar URLs? \n1) Sim \n2)Não"))
    
    if resposta == 1:
        enderecos = [input("Informe endereços Web(URLs) que sempre começam com 'www.'e sempre terminam com '.com' .")]
        URLs = []
        dominios = []
        for endereco in enderecos:
            if (endereco[:4] == 'www.') and (endereco[4:] == '.com'):
                URLs.append(endereco)
                print("URLs: ", URLs)
            
                dominios.append(URLs[5:5])
                print("Domínios: ", dominios)
            
    elif resposta == 2:    
        break
    else:
        print("Opa, o número informado está incorreto. =/")

#questão 03
import random

numeros = []
for i in range(10):
    numeros.append(random.randint(-100,100))
    
ordenada = sorted(numeros)
print("Lista ordenada:", ordenada)

print("Lista original:", numeros)

print("Índice do maior valor da lista:", max(numeros))

print("Índice do menor valor da lista:", min(numeros))

soma = sum(numeros)
print("Soma dos valores da lista:", soma)

media = soma/10
print("Média dos valores da lista:", media)

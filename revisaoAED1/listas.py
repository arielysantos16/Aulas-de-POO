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


#questão 4

lista1 = []
lista2 = []
lista3 = []

quant1 = int(input("Informe a quantidade de elementos da lista 1: "))
for i in range(quant1):
    elemento1 = int(input(f"Digite um dos {quant1} elementos: "))
    lista1.append(elemento1)

quant2 = int(input("Informe a quantidade de elementos da lista 2: "))
for i in range(quant2):
    elemento2 = int(input(f"Digite um dos {quant2} elementos: "))
    lista2.append(elemento2)

#comparar listas
if len(lista1) >= len(lista2):#os remanecentes são da 1
    quant3 = len(lista1)

    for i in range(quant3):
        lista3.append(lista1[i])
        if i < len(lista2):
            lista3.append(lista2[i])  

else:#os remanecentes são da 2
    quant3 = len(lista2)#tamanho lista 3
    
    for i in range(quant3):
        if i < len(lista1):
            lista3.append(lista1[i])
        
        lista3.append(lista2[i])

print('Lista 1:', lista1)

print('Lista 2:', lista2)

print('Alternada:', lista3)

#questão 5 ____ERRO na intersecção
import random

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(random.randint(0,50))

for i in range(20):
    lista2.append(random.randint(0,50))

print('Lista 1:', lista1)
print('Lista 2:', lista2)

print('Intersecção:', sorted(interseccao))

#questão 6 ____ERRO
import random

lista = []
for i in range(20):
    lista.append(random.randint(0,100))
    
print('Lista original: ',lista)

t = int(input('Informe o tamanho em que desejas separar a lista em tamanhos menores: '))
print('Sublistas: ', lista[::t])



#questão 7
import random 

n = int(input('Informe o tamanho da matriz: '))

lista = []
for l in range(n):
    lista.append([l for i in range(n)])

for item in lista:
    print(item)

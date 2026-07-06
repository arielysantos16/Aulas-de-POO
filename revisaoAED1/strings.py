#Questão 01
Nome = input("Informe seu primeiro nome: ")
Sobrenome = input("Informe seu sobrenome: ")
print("Bem Vindo(a), " + Nome + " " + Sobrenome + "!")

#Questão 02

frase = input("Olá! Informe uma frase: ")
print("A quantidade de espaços nessa frase é: ",  frase.count(" "))

#Questão 03
nome = input("Informe seu nome: ")
#print(nome.rsplit(len(nome)))         "rsplit() - Divide a ...string no separador especificado e retorna uma lista"
juntando = ""
for letra in nome:
    juntando += letra
    print(juntando)

#Questão 04
num = input("Informe número de celular:")
if len(num) == 8:
    print("Número completo: 9" + num[0:4] + "-" + num[4:8])
    
elif len(num) == 9:
    if num[0] == "9":
        print(num[0:5] + "-" + num[5:9])
    else:
        print("Erro! \nO número precisa começar com 9(nove).")
        
else:
    print("Erro! \nVerifique o que pode está sendo o seu erro, e tente deixar o número digitado como no modelo abaixo: \nxxxxxxxx ou 9xxxxxxxx")

#Questão 05

frase = input("Digite uma frase")

indice_vogais = [ ]
total = 0
for letra in frase:
    if letra in "aeiou":
        indice_vogal = frase.find(letra)#retorna o índice da vogal
        indice_vogais.append(indice_vogal)
        total += 1 #calcula o total de vogais

print(f"O índice das vogais é {indice_vogais}.")
print(f"O total de vogais é: {total}.")

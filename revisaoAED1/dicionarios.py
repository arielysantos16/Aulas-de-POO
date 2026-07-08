#questão 1
def contagem_caracteres(texto):
    for i in range(len(texto)):
        dic_texto = {'caracteres' : i}
        return dic_texto
    
texto = input("Informe um texto: ")
resultado = contagem_caracteres(texto)
print(resultado)

#questão 2
#não sei como fazer

#questão 3
def Mesclar_Dicionarios(dic_1, dic_2):
    novo_dic = {}
    
dic_1 = {'a': 1, 'b': 2, 'c': 3}
dic_2 = {'b': 4, 'd': 5}
resultado = Mesclar_Dicionarios(dic_1, dic_2)
print(resultado)

#questão 4
def Filtrar_Dicionario(dados, chaves):
    dic = {}

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves = ['a', 'c', 'e']
novo_dic = Filtrar_Dicionario(dados, chaves)
print(novo_dic)

#questão 5
def Resultado_Votacao(votos):
    

votos = [{'João' : 120, 'Ana' : 2},
         {'João' : 110, 'Ana' : 22},
         {'João' : 130, 'Ana' : 12},
        ]

eleito = Resultado_Votacao(votos)
print(eleito)

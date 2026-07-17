# Listas suportam varios valores de varios tipos
# tipo list - mutavel
# metodos uteis:
# append (insere no final da lista),
# insert (insere em um determinado indice),
# pop (apaga o ultimo item da lista),
# del (apaga um item da lista),
# clear (limpa a lista),
# extend
# CRUD - Creat, Read, Update, Delete

# lista_a = [123, True, 'Ricardo paiva', 1.2, 'joaquim']
# lista_b = [1, 2, 3, 4]
# lista_c = ['ana', 'syntia', 'duda']
# print(lista_a)
# lista_a.extend(lista_b)
# print(lista_a)
# lista_a.extend(lista_c)
# print(lista_a)
# lista_b.clear()
# print(lista_b)
# print(lista_a)
#
# del lista[2]
# print(lista)
# item = 'faca'
# lista.pop()
# print(lista)
# lista[2] = item
# print(lista)
# lista.insert(0, "eduarda")
# print(lista)

# ---------------------////////-----------------------------------------------------------------------
#
# for in com listas
# Exibir o indice junto ao valor do indice:
#
# lista = ['ricardo', 'duda', 'sintya', 'debora']
#
# for i in range(len(lista)):
#     print(f'{i} - {lista[i]}')

# ------------------------//--------------------------------------------
# Empacotamento:
#
# frutas = ['banana', 'maca', 'morango', 'uva']
# fruta1, fruta2, fruta3, fruta4 = frutas
# print(fruta1)

#----------------------///-------------------------------------------

# Tuplas - uma lista imutavel
# declaradas sem colchetes ou com parenteses
# nomes = 'maria', 'alberto', 'joaquim'
# print(nomes)
#---------------//---------------------------------------------------------

# Enumerando os indices
#
# lista = ['joao', 'maria', 'feijao', 'duda']
# lista_enumerada = tuple(enumerate(lista))
# for indice, nome in lista_enumerada:
#     print(f'{indice} - {nome}')
# ---------------//-----------------------------------------------------------

# Imprecisao de ponto flutuante
#
# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2
# print(numero_3)
# print(f'{numero_3:.2f}') formata as casas decimais
#-------------------------//--------------------------------------------------

# Split e join com list e str
# Split() - divide uma String
# .Join() - une uma string

# frase  = 'Que coisa mais fofa'
# lista_palavras = frase.split()
# print(frase.split('f'))
# print("".join(lista_palavras))
#--------------------------//_______________________________________________

# Listas dentro de listas

# salas = [
#     ['Maria', 'Helena'], ['Elaine', ], ['Luiz', 'Joao', 'Eduarda']
# ]
# print(salas[0][1])
# print(salas[2][2])
# for i, sala in enumerate(salas):
#     print(f'Sala {i} - Alunos: {', '.join(sala)}')
#-----------------//---------------------------------------------------------


import os

def exibir_lista(listas):
    lista_enumerada = enumerate(lista)
    if len(lista) == 0:
        print('Sua lista está vazia. ')
    else:
        for i, item in lista_enumerada:
            print(f'{i} - {item}')

print('__________________//____________________')
print('            LISTA DE COMPRAS                 ')
#print('------------------//-------------------------')
#print()
lista = ['pao', 'presunto', 'manteiga']

while True:
    lista_de_opcoes = ['i', 'a', 'l', 'd', 's']
    print('_________________//_____________________')
    print('Selecione uma Opcao:                 ')
    print('[I]nserir_item  |  [A]pagar_item ')
    print('[L]istar        |  [D]eletar_lista ')
    print('[S]air')
    print('________________________________________')

    opcao = input('-> ').lower()

    if opcao not in lista_de_opcoes:
        os.system('cls')
        print('❌ OPCAO INVALIDA, TENTE NOVAMENTE!')
        continue

    elif opcao.lower() == 'i':
        os.system('cls')
        print('Insira um item: ')
        item = input('-> ')
        lista.append(item)
        print(f'✔ {item.upper()} foi inserido a sua lista\n')
        continue

    elif opcao.lower() == 'a':
        os.system('cls')
        print('Escolha um Indice da lista para apagar: ')
        exibir_lista(lista)
        indice_str = input('-> ')
        try:
            indice_int = int(indice_str)
            if indice_int in range(len(lista)):
                item = lista[indice_int]
                os.system('cls')
                del lista[indice_int]
                print(f'O item {item} do indice {indice_int} foi apagado da sua lista ')
            else:
                print(f'Indice "{indice_int}" nao existe na sua lista ')
        except ValueError:
            print(f'Indice "{indice_str}" nao existe na sua lista ')

    elif opcao.lower() == 'l':
        os.system('cls')
        exibir_lista(lista)

    elif opcao.lower() == 'd':
        os.system('cls')
        lista.clear()
        print('Sua lista foi deletada')

    elif opcao.lower() == 's':
        os.system('cls')
        print('Encerrando . . .')
        break
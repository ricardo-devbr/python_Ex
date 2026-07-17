from faker import Faker

## APLICAR IA PARA SELECIONAR A PALAVRA POR CATEGORIA E DAR DICAS
## BASEADA EM CARAACTERISTICAS DA PALAVRA ESCOLHIDA
print('----------------//---------------')
print('JOGO DA PALAVRA SECRETA')
print('----------------//---------------\n')

print('Escolha uma letra e adivinhe a palavra secreta')
print("Voce possui 5 tentativas")

gerador = Faker('pt_BR')
palavraSecreta = gerador.word()
tentivas = 5
letrasCertas = ''

while True:

    letraEscolhida = input("Qual letra voce quer escolher ? ")
    print(f'{tentivas} tentativas')
    palavraFormada = ''

    if len(letraEscolhida) > 1:
        print('Voce deve escolher somente UMA letra!')
        continue

    if letraEscolhida in palavraSecreta:
        letrasCertas += letraEscolhida
    else:
        tentivas -= 1
        print(f'Voce errou, restam {tentivas} tentativas')

    for i in palavraSecreta:
        if i in letrasCertas:
            palavraFormada += i
        else:
            palavraFormada += '_'
    print(' '.join(palavraFormada))

    if palavraFormada == palavraSecreta:
        print(f"Voce venceu!!! A palavra secreta é {palavraSecreta.upper()}")
        break
    elif tentivas == 0:
        print('Tentativas esgotadas, voce perdeu!')
        break
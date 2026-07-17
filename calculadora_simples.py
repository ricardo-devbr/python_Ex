
print("----------------\\-------------")
print("CALCULADORA SIMPLES")
print("----------------\\-------------")

while True:

    print("ESCOLHA UMA OPCAO \n")
    print("1 - CALCULAR")
    print('2 - SAIR')
    opcao = input()

    if opcao == "1":
        try:
            numero1 = int(input('DIGITE UM NUMERO PARA CALCULAR '))
            operacao = input('escolha a operacao: +, -, x, / \n')

            if operacao not in ['+', '-', 'x', '/']:
                print('OPERACAO INVALIDA! ESCOLHA ENTRE: +, -, x, /.\n')
                continue
            numero2 = int(input('DIGITE UM NUMERO PARA CALCULAR \n'))
            resultado = 0

            match operacao:
                case '+':
                    resultado = numero1 + numero2
                case '-':
                    resultado = numero1 - numero2
                case 'x':
                    resultado = numero1 * numero2
                case '/':
                    resultado = numero / numero2
            print(f'{numero1} {operacao} {numero2} = {resultado}\n')

        except ValueError:
            print('DIGITO INVALIDO! TENTE NOVAMENTE\n')

    elif opcao == '2':
        print('ENCERRANDO . . .')
        break

    elif opcao !=1 or opcao != 2:
        print('OPCAO INVALIDA! TENTE NOVAMENTE')

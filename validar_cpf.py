import random

def gerar_cpf(cpf):
    cont_regressivo = 10
    soma_resultados = 0

    print('A soma dos 9 primeiros digitos do cpf multiplicando cada digito por\n'
          'uma contagem regressiva partindo de 10\n')

    for digito_1 in cpf_nove_digitos:
        resultado = int(digito_1) * int(cont_regressivo)
        print(f'N° Cpf {digito_1} x {cont_regressivo} = {resultado}')
        soma_resultados += resultado
        cont_regressivo -= 1
    print(f'\nA soma dos resultados é *{soma_resultados}*\n')

    resultado_x10 = soma_resultados * 10
    resto_por11 = resultado_x10 % 11

    print(f'Soma dos resultados multiplicado por 10:\n'
          f'{soma_resultados} * 10 = {resultado_x10}\n')

    print(f'O resto da divisao da soma dos resultados por 11:'
          f'\n{resultado_x10} % 11 = {resto_por11}\n')

    if resto_por11 > 9:
        primeiro_dig = 0
        print(f'O primeiro digito do cpf deve ser {primeiro_dig}')
    else:
        primeiro_dig = resto_por11
        print(f'O primeiro digito do cpf deve ser {primeiro_dig}\n')

    cpf_10_digitos = cpf_nove_digitos + str(primeiro_dig)
    print(f'Seu cpf é {cpf_10_digitos}')
    print()

    cont_regressivo_2 = 11
    soma_resultados_2 = 0

    print('A soma dos 10 primeiros digitos do cpf multiplicando cada digito por\n'
          'uma contagem regressiva partindo de 11\n')

    for digito_2 in cpf_10_digitos:
        resultado_2 = int(digito_2) * int(cont_regressivo_2)
        print(f'N° Cpf {digito_2} x {cont_regressivo_2} = {resultado_2}')
        soma_resultados_2 += resultado_2
        cont_regressivo_2 -= 1
    print(f'\nA soma dos resultados é *{soma_resultados_2}*\n')

    resultado_x10_2 = soma_resultados_2 * 10
    resto_por11_2 = resultado_x10_2 % 11

    print(f'Soma dos resultados multiplicado por 10:\n'
          f'{soma_resultados_2} * 10 = {resultado_x10_2}\n')

    print(f'O resto da divisao da soma dos resultados por 11:'
          f'\n{resultado_x10_2} % 11 = {resto_por11_2}\n')

    if resto_por11_2 > 9:
        segundo_dig = 0
        print(f'O segundo digito do cpf deve ser {segundo_dig}')
    else:
        segundo_dig = resto_por11_2
        print(f'O segundo digito do cpf deve ser {segundo_dig}\n')
    novo_cpf = str(cpf_nove_digitos) + str(primeiro_dig) + str(segundo_dig)
    print(novo_cpf)

print('--------------------------------')
print('GERADOR e VALIDADOR DE CPF: ')
print('--------------------------------')
print('SELECIONE UMA OPCAO: \n')
opcao = int(input('1 - Gerar CPF.\n2 - Validar CPF.\n'))

if opcao == 1:
    cpf_nove_digitos = ''
    sample = random.sample(range(9),9)
    for i in sample:
        cpf_nove_digitos += str(i)
    gerar_cpf(cpf_nove_digitos)

# def gerar_cpf(cpf):
#     cont_regressivo = 10
#     soma_resultados = 0
#
#     print('A soma dos 9 primeiros digitos do cpf multiplicando cada digito por\n'
#           'uma contagem regressiva partindo de 10\n')
#
#     for digito_1 in cpf_nove_digitos:
#         resultado = int(digito_1) * int(cont_regressivo)
#         print(f'N° Cpf {digito_1} x {cont_regressivo} = {resultado}')
#         soma_resultados += resultado
#         cont_regressivo -= 1
#     print(f'\nA soma dos resultados é *{soma_resultados}*\n')
#
#     resultado_x10 = soma_resultados * 10
#     resto_por11 = resultado_x10 % 11
#
#     print(f'Soma dos resultados multiplicado por 10:\n'
#           f'{soma_resultados} * 10 = {resultado_x10}\n')
#
#     print(f'O resto da divisao da soma dos resultados por 11:'
#           f'\n{resultado_x10} % 11 = {resto_por11}\n')
#
#     if resto_por11 > 9:
#         primeiro_dig = 0
#         print(f'O primeiro digito do cpf deve ser {primeiro_dig}')
#     else:
#         primeiro_dig = resto_por11
#         print(f'O primeiro digito do cpf deve ser {primeiro_dig}\n')
#
#     cpf_10_digitos = cpf_nove_digitos + str(primeiro_dig)
#     print(f'Seu cpf é {cpf_10_digitos}')
#     print()
#
#     cont_regressivo_2 = 11
#     soma_resultados_2 = 0
#
#     print('A soma dos 10 primeiros digitos do cpf multiplicando cada digito por\n'
#           'uma contagem regressiva partindo de 11\n')
#
#     for digito_2 in cpf_10_digitos:
#         resultado_2 = int(digito_2) * int(cont_regressivo_2)
#         print(f'N° Cpf {digito_2} x {cont_regressivo_2} = {resultado_2}')
#         soma_resultados_2 += resultado_2
#         cont_regressivo_2 -= 1
#     print(f'\nA soma dos resultados é *{soma_resultados_2}*\n')
#
#     resultado_x10_2 = soma_resultados_2 * 10
#     resto_por11_2 = resultado_x10_2 % 11
#
#     print(f'Soma dos resultados multiplicado por 10:\n'
#           f'{soma_resultados_2} * 10 = {resultado_x10_2}\n')
#
#     print(f'O resto da divisao da soma dos resultados por 11:'
#           f'\n{resultado_x10_2} % 11 = {resto_por11_2}\n')
#
#     if resto_por11_2 > 9:
#         segundo_dig = 0
#         print(f'O primeiro digito do cpf deve ser {segundo_dig}')
#     else:
#         segundo_dig = resto_por11_2
#         print(f'O primeiro digito do cpf deve ser {segundo_dig}\n')
#     novo_cpf = str(cpf_nove_digitos) + str(primeiro_dig) + str(segundo_dig)
#     print(f"CPF gerado: {novo_cpf}")
#
elif opcao == 2:
    print('___VALIDADOR DE CPF___ \n')

    cpf_usuario = input('Insira um CPF para validar: ')
    cpf_usuario_formatado = cpf_usuario.replace('-','.').replace('.','')
    cpf_nove_digitos = (cpf_usuario_formatado[:9])
    gerar_cpf(cpf_nove_digitos)
#
#     cont_regressivo = 10
#     soma_resultados = 0
#
#     print('A soma dos 9 primeiros digitos do cpf multiplicando cada digito por\n'
#           'uma contagem regressiva partindo de 10\n')
#
#     for digito_1 in cpf_9_digitos:
#         resultado = int(digito_1) * int(cont_regressivo)
#         print(f'N° Cpf {digito_1} x {cont_regressivo} = {resultado}')
#         soma_resultados += resultado
#         cont_regressivo -= 1
#     print(f'\nA soma dos resultados é *{soma_resultados}*\n')
#
#     resultado_x10 = soma_resultados * 10
#     resto_por11 = resultado_x10 % 11
#
#     print(f'Soma dos resultados multiplicado por 10:\n'
#           f'{soma_resultados} * 10 = {resultado_x10}\n')
#
#     print(f'O resto da divisao da soma dos resultados por 11:'
#           f'\n{resultado_x10} % 11 = {resto_por11}\n')
#
#     if resto_por11 > 9:
#         primeiro_dig = 0
#         print(f'O primeiro digito do cpf deve ser {primeiro_dig}')
#     else:
#         primeiro_dig = resto_por11
#         print(f'O primeiro digito do cpf deve ser {primeiro_dig}\n')
#
# # ----------------------------------------------------------------------------------
#
#     print('\nCALCULO DO SEGUNDO DIGITO DE UM CPF:\n')
#
#     cpf_10_digitos = cpf_9_digitos + str(primeiro_dig)
#     print(f'Seu cpf é {cpf_10_digitos}')
#     print()
#
#     cont_regressivo_2 = 11
#     soma_resultados_2 = 0
#
#     print('A soma dos 10 primeiros digitos do cpf multiplicando cada digito por\n'
#           'uma contagem regressiva partindo de 11\n')
#
#     for digito_2 in cpf_10_digitos:
#         resultado_2 = int(digito_2) * int(cont_regressivo_2)
#         print(f'N° Cpf {digito_2} x {cont_regressivo_2} = {resultado_2}')
#         soma_resultados_2 += resultado_2
#         cont_regressivo_2 -= 1
#     print(f'\nA soma dos resultados é *{soma_resultados_2}*\n')
#
#     resultado_x10_2 = soma_resultados_2 * 10
#     resto_por11_2 = resultado_x10_2 % 11
#
#     print(f'Soma dos resultados multiplicado por 10:\n'
#           f'{soma_resultados_2} * 10 = {resultado_x10_2}\n')
#
#     print(f'O resto da divisao da soma dos resultados por 11:'
#           f'\n{resultado_x10_2} % 11 = {resto_por11_2}\n')
#
#     if resto_por11_2 > 9:
#         segundo_dig = 0
#         print(f'O segundo digito do cpf deve ser {segundo_dig}')
#     else:
#         segundo_dig = resto_por11_2
#         print(f'O segundo digito do cpf deve ser {segundo_dig}\n')
#
# # ----------------------------------------------------------------------------
#     novo_cpf = str(cpf_9_digitos) + str(primeiro_dig) + str(segundo_dig)
#
#     if cpf_usuario_formatado == novo_cpf:
#         print('O CPF é válido ✔')
#     else:
#         print('O CPF nao é válido ❌')
# -------------------------------------------------------------------------------------




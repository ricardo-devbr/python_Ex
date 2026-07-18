import random

def gerar_cpf(cpf):
    cont_regressivo = 10
    soma_resultados = 0

# A soma dos 9 primeiros digitos do cpf multiplicando cada digito por uma contagem regressiva partindo de 10

    for digito_1 in cpf_nove_digitos:
        resultado = int(digito_1) * int(cont_regressivo)
        soma_resultados += resultado
        cont_regressivo -= 1

# Soma dos resultados multiplicado por 10
    resultado_x10 = soma_resultados * 10
# O resto da divisao da soma dos resultados por 11
    resto_por11 = resultado_x10 % 11

# O primeiro digito do cpf deve ser igual a 0 se o resto por 11 for maior que 9
    if resto_por11 > 9:
        primeiro_dig = 0
# Se nao, o primeiro digito deve ser igual ao resultado de resto por 11
    else:
        primeiro_dig = resto_por11

# Adiciona o primeiro digito calculado os 9 primeiros digitos do CPF
    cpf_10_digitos = cpf_nove_digitos + str(primeiro_dig)

    cont_regressivo_2 = 11
    soma_resultados_2 = 0

# A soma dos 10 primeiros digitos do cpf multiplicando cada digito por uma contagem regressiva partindo de 11
    for digito_2 in cpf_10_digitos:
        resultado_2 = int(digito_2) * int(cont_regressivo_2)
        soma_resultados_2 += resultado_2
        cont_regressivo_2 -= 1

    resultado_x10_2 = soma_resultados_2 * 10
    resto_por11_2 = resultado_x10_2 % 11

# O segundo digito do cpf deve ser 0 se o resto por 11 for maior que 9
    if resto_por11_2 > 9:
        segundo_dig = 0
# Se nao, o segundo digito deve ser o resultado do resto por 11
    else:
        segundo_dig = resto_por11_2
    novo_cpf = str(cpf_nove_digitos) + str(primeiro_dig) + str(segundo_dig)
    # print(f'O CPF gerado é {novo_cpf}')
    return novo_cpf

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
    print(f"O CPF gerado é {gerar_cpf(cpf_nove_digitos)}")

elif opcao == 2:
    print('___VALIDADOR DE CPF___ \n')

    cpf_usuario = input('Insira um CPF para validar: ')
    cpf_usuario_formatado = cpf_usuario.replace('-','.').replace('.','')
    cpf_nove_digitos = str(cpf_usuario_formatado[:9])

    if cpf_usuario_formatado == gerar_cpf(cpf_nove_digitos):
        print(f'O CPF {cpf_nove_digitos} é válido ✔')
    else:
        print(f'O CPF {cpf_nove_digitos} nao é válido ❌')
"""Calculadora com while"""

import os

while True:
    
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')

    try:
        float_numero_1 = float(numero_1)
        float_numero_2 = float(numero_2)
        
        if isinstance(float_numero_1, float) and isinstance(float_numero_2, float):
            operador = input('Selecione algum operador ([+] [-] [/] [*]): ')
        elif isinstance(float_numero_1, int) and isinstance(float_numero_2, int):
            operador = input('Selecione algum operador ([+] [-] [/] [*]): ')
        elif isinstance(float_numero_1, int) and isinstance(float_numero_2, float):
            operador = input('Selecione algum operador ([+] [-] [/] [*]): ')
        elif isinstance(float_numero_1, float) and isinstance(float_numero_2, int):
            operador = input('Selecione algum operador ([+] [-] [/] [*]): ')
    except:
        os.system('cls')
        print(input('Algum número está invalido, aperte qualquer tecla para reiniciar a calculadora: '))
        os.system('cls')
        continue

    if operador == '+':
        print('Calculando...')
        print(float_numero_1 + float_numero_2)
    elif operador == '-':
        print('Calculando...')
        print(float_numero_1 - float_numero_2)
    elif operador == '/':
        print('Calculando...')
        print(float_numero_1 / float_numero_2)
    elif operador == '*':
        print('Calculando...')
        print(float_numero_1 * float_numero_2)
    else:
        print('Operador inválido')
        invalido = (input('deseja tentar novamente? [S]im [N]ão: '))
        invalido = invalido.lower()

        if invalido == 's':
            os.system('cls')
            continue
        else:
            os.system('cls')
            break 

    repetir = input('Deseja calcular novamente? [S]im [N]ão. ')
    repetir = repetir.lower()

    if repetir == 's':
        os.system('cls')
        continue
    else:
        os.system('cls')
        break
    
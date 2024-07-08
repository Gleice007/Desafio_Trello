"""
1º Escreva um programa que recebe um número inteiro do usuário e imprime
se ele é um número é par ou ímpar.
"""

entrada = input('Informe um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'O número {entrada_int} é {par_impar_texto}')  

else:
    print('Esse número não é inteiro')      
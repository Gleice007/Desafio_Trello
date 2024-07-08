"""
Desenvolva uma calculadora simples que recebe dois números e um
operador (+, -, *, /) do usuário e realiza a operação correspondente.
"""

print("Calculadora Simples")
print("Operações disponíveis:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("\nEscolha a operação desejada (1-4): ")

if opcao in {'1', '2', '3', '4'}:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = num1 + num2
        operacao = '+'
    elif opcao == '2':
        resultado = num1 - num2
        operacao = '-'
    elif opcao == '3':
        resultado = num1 * num2
        operacao = '*'
    elif opcao == '4':
        if num2 != 0:
            resultado = num1 / num2
            operacao = '/'
        else:
            resultado = "Erro! Divisão por zero não é permitida."
            operacao = '/'
    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
else:
    print("Opção invalida! Escolha uma opção válida (1-4).")         
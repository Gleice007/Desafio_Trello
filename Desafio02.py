def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0 

    for char in texto:
        if char in vogais:
            contador += 1
    return contador

entrada = input('Digite o seu nome completo: ')

num_vogais = contar_vogais(entrada)

print(f'O número de vogais no texto é {num_vogais}')

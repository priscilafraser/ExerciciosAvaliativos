""" 
07 - Crie um programa onde o usuário possa digitar sete valores 
# numéricos e cadastre-os em uma lista única que mantenha 
# separados os valores pares e ímpares. No final, mostre os 
# valores pares e ímpares em ordem crescente. """

valor = []
par = impar = []
c = 0

for c in range(0,8):
    par = []
    impar = []
    while len(valor) < 7:
        valor.append(int(input('Digite um número: ')))
    for i in valor:
        if i % 2 == 0:
            par.append(i)
            par.sort()
        else:
            impar.append(i)
            impar.sort()

valor.clear()
valor.append(par)
valor.append(impar)


print(f'A lista par é {par}')
print(f'A lista ímpar é {impar}')
print(f'A lista final é {valor}')
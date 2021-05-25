
print('Digite dois números: ')

num1 = int(input('Digite o primeiro: '))
num2 = int(input('Digite o segundo: '))

soma = num1 + num2
multi = num1 * num2
divInt = num1 // num2

print(f'A soma deles é {soma}')
print(f'A multiplicação entre eles é {multi}')
print(f'A divisão inteira deles é {divInt}')

if num1 > num2:
    print(f'{num1} é o maior número')
else:
    print(f'{num2} é o maior número')

if soma % 2 == 0:
    print(f'O resultado da soma é par')
else:
    print(f'O resultado da soma é ímpar')

if multi > 40:
    if divInt == 0:
        print('A divisão por 0 é indefinida')
    else:
        x = multi / divInt
        print(x)
else:
    print('A multiplicação não foi maior que 40')
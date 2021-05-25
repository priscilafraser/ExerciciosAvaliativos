frases = []

frases.append("Telefonou para a vítima? ")
frases.append("Esteve no local do crime? ")
frases.append("Mora perto da vítima? ")
frases.append("Devia para a vítima? ")
frases.append("Já trabalhou com a vítima? ")

s = 0
n = 0
resposta = 0

for i in frases:
    frases = input(f'{i}Responda S/N:').upper()
    if frases == 'S':
        s += 1
    elif frases == 'N':
        n += 1
    elif frases not in 'SN':
        while frases != 'S' and frases != 'N':
            print('Resposta inválida. Tente Novamente!')
            frases = input(i).upper()


print(f'Foram {s} resposta(s) positivas') 
print(f'Foram {n} resposta(s) negativas')

print('-' * 50)

if s == 2:
    print('As respostas indicam como "Suspeito"')
elif s >= 3 and s <= 4:
    print('As respostas indicam como "Cúmplice"')
elif s == 5:
    print('As respostas indicam como "Assassino"')
else:
    print('As respostas indicam como "Inocente"')
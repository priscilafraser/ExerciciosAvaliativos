""" 02 - Utilizando estruturas de repetição com variável de 
controle, faça um programa que receba uma string com uma 
frase informada pelo usuário e conte quantas vezes aparece 
as vogais a,e,i,o,u e mostre na tela, depois mostre na tela
 essa mesma frase sem nenhuma vogal. """


frase = str(input('Digite sua frase: '))
a = 0
e = i = o = u = 0

for f in frase:
    if f == 'a' or f == 'á' or f == 'ã' or f == 'â' or f == 'à' or f == 'A' or f == 'Á' or f == 'Ã' or f == 'Â' or f == 'À':
        a += 1
    elif f == 'e' or f == 'é' or f == 'ê' or f == 'E' or f == 'É' or f == 'Ê':
        e += 1
    elif f == 'i' or f == 'í' or f == 'I' or f == 'Í':
        i += 1
    elif f == 'o' or f == 'ó' or f == 'ô' or f == 'õ' or f == 'O' or f == 'Ó' or f == 'Ô' or f == 'Õ':
        o += 1
    elif f == 'u' or f == 'ú' or f == 'U' or f == 'Ú':
        u += 1


print(f'A letra a aparece {a} vezes')
print(f'A letra e aparece {e} vezes')
print(f'A letra i aparece {i} vezes')
print(f'A letra o aparece {o} vezes')
print(f'A letra u aparece {u} vezes')
print(frase.replace('a', ' ').replace('á', ' ').replace('â', ' ').replace('ã', ' ')
    .replace('à', ' ').replace('e', ' ').replace('é', ' '). replace('ê', ' ').replace('i', ' ')
    .replace('í', ' ').replace('o', ' ').replace('ó', ' ').replace('ô', ' ')
    .replace('õ', ' ').replace('u', ' ').replace('ú', ' ')
    .replace('A', ' ').replace('Á', ' ').replace('Â', ' ')
    .replace('Ã', ' ').replace('À', ' ').replace('É', ' ')
    .replace('E', ' ').replace('Ê', ' ').replace('I', ' ')
    .replace('Í', ' ').replace('O', ' ').replace('Ó', ' ')
    .replace('Ô', ' ').replace('Õ', ' ').replace('U', ' ')
    .replace('Ú', ' '))

#Testar = alámâpãkà elévê índio ôlóvõ burú
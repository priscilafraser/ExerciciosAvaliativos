""" 05 - Refatore o exercício 2, para que uma função receba a frase,
faça todo o tratamento necessário e retorne o resultado. Depois 
mostre na tela o resultado e a quantidade de letras foram 
retiradas da frase original. """

def frase(x):
    #frase = input('Digite sua frase: ')
    a = e = i = o = u = 0
    c = 0

    for f in x:
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
        if f in 'aáâãàAÁÂÃÀeéêEÉÊiíIÍoóôõOÓÔÕuúUÚ':
            c = c + 1
    
    print(f'A letra a aparece {a} vezes')
    print(f'A letra e aparece {e} vezes')
    print(f'A letra i aparece {i} vezes')
    print(f'A letra o aparece {o} vezes')
    print(f'A letra u aparece {u} vezes')
    print(x.replace('a', ' ').replace('á', ' ').replace('â', ' ').replace('ã', ' ')
    .replace('à', ' ').replace('e', ' ').replace('é', ' '). replace('ê', ' ').replace('i', ' ')
    .replace('í', ' ').replace('o', ' ').replace('ó', ' ').replace('ô', ' ')
    .replace('õ', ' ').replace('u', ' ').replace('ú', ' ')
    .replace('A', ' ').replace('Á', ' ').replace('Â', ' ')
    .replace('Ã', ' ').replace('À', ' ').replace('É', ' ')
    .replace('E', ' ').replace('Ê', ' ').replace('I', ' ')
    .replace('Í', ' ').replace('O', ' ').replace('Ó', ' ')
    .replace('Ô', ' ').replace('Õ', ' ').replace('U', ' ')
    .replace('Ú', ' '))
    print(f'Foram retiradas {c} letras da frase original')
    


frase(input('Digite uma frase: '))

#Testar = alámâpãkà elévê índio ôlóvõ burú
""" 04 - Utilizando funções e listas faça um programa que receba 
uma data no formato DD/MM/AAAA e devolva uma string no formato 
DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 
'data inválida' caso a data seja inválida. """


data = input('Digite a data no formato dd/mm/aaaa: ')

def mesExtenso(x):
    mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'sep', 'out', 'nov', 'dez']
    if x in '/01/':
        return x



mesExtenso(data)

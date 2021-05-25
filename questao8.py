import datetime

cadastro = dict()

cadastro['Nome'] = input('Digite seu nome: ')
cadastro['Nascimento'] = int(input('Digite o ano do seu nascimento: '))
cadastro['CTPS'] = int(input('Anos de carteira assinada: '))
hoje = datetime.date.today().year
cadastro['Idade'] = hoje - cadastro['Nascimento']
contribuicao = 35

if cadastro['CTPS'] != 0:
    cadastro['Ano de Contrato'] = int(input('Digite o ano da contratação: '))
    cadastro['Salario'] = float(input('Digite o salário: '))
    contFalta = contribuicao - cadastro['CTPS']
    cadastro['Idade Aposentadoria'] = cadastro['Idade'] + contFalta
    print(cadastro)
else:
    print('Fim do cadastro')
    print(cadastro)


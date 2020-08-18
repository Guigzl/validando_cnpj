import re

cnpj = input('passa o cnpj ae: ')
f_cnpj = list(re.sub(r'[^0-9]', '', cnpj))
cnpj = re.sub(r'[^0-9]', '', cnpj)
cnpj = list(cnpj[0:12])


def formulacao(param):
    form = 11 - (param % 11)
    if form < 9:
        cnpj.append(str(form))
    else:
        cnpj.append('0')


cont = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
comb = list(zip(cnpj, cont))
soma = []

for x, y in comb:
    res = int(x) * y
    soma.append(res)
soma = sum(soma)

formulacao(soma)

cont2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
comb2 = zip(cnpj, cont2)
comb2 = list(comb2)
soma2 = []

for k, v in comb2:
    res2 = int(k) * v
    soma2.append(res2)
soma2 = sum(soma2)

formulacao(soma2)

if cnpj == f_cnpj:
    print('Validou')
else:
    print('nao validou meu kerido')

import random as r

lista = []
lista_impar =[]
lista_par = []
i = 1

while i <= 10:
    lista.append(r.randrange(1,100,3))
    i = i+1

print(f'essa foi a lista gerada aleatoriamente: {lista}')

for n in lista:
    if n % 2 != 0:
        lista_impar.append(n)
    else:
        lista_par.append(n)

print(f'impares:{lista_impar}')
print(f'pares:{lista_par}')    
import random as r

lista = []
i = 1

while i <= 10:
    lista.append(r.randrange(1,200,3))
    i = i+1

print(f'essa foi a lista gerada aleatoriamente: {lista}')

def maior_valor(lista):
    return max(lista, key=int)

print(f'maior valor é: {maior_valor(lista)}')    
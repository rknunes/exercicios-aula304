def numero_par(a):
    numero = (a) %2 == 0
    return numero

n1 = int(input('Escolha um número inteiro: '))

if (n1) %2 == 0:
    print('O número é par.') 

else:
    print('O número é impar.')
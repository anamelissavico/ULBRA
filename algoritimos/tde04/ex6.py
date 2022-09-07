from cmath import sqrt


n1=int(input('Digite um número\n'))
n2=int(input('Digite outro número\n'))
n3=int(input('Digite mais um número\n'))
if n1>0:
    import math
    raiz= sqrt(n1)
    print(f'A raíz quadrada de primeiro número é {raiz}')
else:
    quad:n1*n1
    print(f'O primeiro número ao quadrado é {quad}')

if n2>10 and n2<100:
    print(f'NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO')

elif n3<n2:
    dif=n3%n2
    print(f'A difereça entre o terceiro número e o segundo é {dif}')
else:
    soma=n3+n2
    print(f'A soma entre o terceiro número e o segundo é {soma}')
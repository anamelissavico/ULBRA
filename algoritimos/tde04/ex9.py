n1=int(input(f'Digite um número\n'))
n2=int(input(f'Digite outro número\n'))
n3=int(input('Digite mais um número\n'))
if n1>n2 and n1>n3:
    print (n1)
elif n2>n1 and n1>n3:
    print(n2)
else:
    print (n3)
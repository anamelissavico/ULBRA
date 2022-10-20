x=0

while x <=5:
    numero=int(input("Digite o número:\n"))
    if numero == 0:
        print(f'Valor igual a zero, nulo.')
    elif numero > 0:
        print(f'Valor positivo.')
    else:
        print(f'Valor negativo')
    x=x+1
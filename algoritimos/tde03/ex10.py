num_vendedor=int(input('Digite seu número\n'))
salario=float(input('Qual o seu sálario fixo?\n'))
carros=int(input('Quantos carros você vendeu esse mês?\n'))
comissao=float(input('Qual sua comissão por carro?\n'))
total= (carros*comissao)+salario
print(f'Vendedor {num_vendedor} seu salário esse mês vai ser de {total}!')

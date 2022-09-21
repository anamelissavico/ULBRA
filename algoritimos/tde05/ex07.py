nome= input('Digite o seu nome:\n')
s_a=float(input('Qual o valor do seu salario atual?\n'))

if s_a >=0 and s_a <= 400:
    novo_salario=s_a*1.15
    print(f'o percentual de aumento foi de 15% e o valor reajustado é de R$ {novo_salario:.2f}')
elif s_a>400 and s_a<700:
    novo_salario=s_a*1.12
    print(f'o percentual de aumento foi de 12% e o valor reajustado é de R$ {novo_salario:.2f}')
elif s_a >700 and s_a<1000:
    novo_salario=s_a*1.10
    print(f'o percentual de aumento foi de 10% e o valor reajustado é de R$ {novo_salario:.2f}')
elif s_a>1000 and s_a<1800:
    novo_salario=s_a*1.07
    print(f'o percentual de aumento foi de 7% e o valor reajustado é de R$ {novo_salario:.2f}')
elif s_a >1800 and s_a<2500:
    novo_salario=s_a*1.04
    print(f'o percentual de aumento foi de 4% e o valor reajustado é de R$ {novo_salario:.2f}')
else:
    print(f'seu salario é maior que R$ 2.500,00 por isso nao teve reajuste')

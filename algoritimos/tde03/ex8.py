alt=float(input('Qual a altura do cilindro?\n'))
raio=float(input('Qual o raio do cilindro?\n'))
preco= 150
litro=5
a_base= 3.14*(raio*raio)
a_lateral= (raio*alt)*3.14*2
a_total= a_base+a_lateral
pintura=a_total/15
custo=pintura*150
print(f'Vão ser necssárias {pintura} latas e o custo delas será {custo} reais.')

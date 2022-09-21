cd_aluno=int(input('Digite o código do aluno\n'))
nota1= float(input('Digite sua nota 1:\n'))
nota2= float(input('Digite sua nota 2:\n'))
nota3= float (input('Digite sua nota 3:\n'))

mediaPonderada = (nota1 * 4 + nota2 * 3 + nota3 * 3 ) / 10

print (f'Seu código é {cd_aluno}')
print(nota1)
print(nota2)
print(nota3)

if mediaPonderada>= 9.0:
    conceito="A"
elif mediaPonderada>= 7.5:
    conceito="B"
elif mediaPonderada>=6.0:
    conceito="C"
elif mediaPonderada>=4:
    conceito="E" 

if conceito =="A" or conceito=="B":
    print(f'Parabéns você foi aprovado!')
else:
    print(f'Você foi reprovado :(')

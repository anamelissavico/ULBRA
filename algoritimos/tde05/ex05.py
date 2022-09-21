codigo_aluno= int(input("Digite o código do aluno:\n"))
nota_a= float (input("Digite a primeira nota:\n"))
nota_b= float (input("Digite a segunda nota:\n"))
nota_c= float (input("Digite a terceira nota:\n"))
maior_nota= max (nota_a,nota_b,nota_c)
nota_peso4= maior_nota *4
menores_notas=(nota_a+nota_b+nota_c) - maior_nota
nota_peso3= menores_notas *3
media=(nota_peso3+nota_peso4)/(3+3+4)

if media >= 7:
    print(f"O aluno código {codigo_aluno} com notas {nota_a}, {nota_b}, {nota_c}, com uma média de {media} está aprovado.")
else:
    print(f"O aluno código {codigo_aluno} com notas {nota_a}, {nota_b}, {nota_c}, com uma média de {media} está reprovado.")

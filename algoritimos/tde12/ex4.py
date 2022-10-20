x=0
total=0

for x in range (10):
    nota=int(input('Digite sua nota:\n'))
    total=total+nota
    x=x+1
media=total/10
print(f'A média da turma é {media}')

from statistics import median


x=0
total=0

while x<10:
    nota=int(input('Digite sua nota:\n'))
    total=total+nota
    x=x+1
media=total/10
print(f'A média da turma é {media}')




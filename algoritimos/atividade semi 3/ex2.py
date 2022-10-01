parede=float(input('Qual a medida da sua parede em m²?:\n'))
tipo_tijolo=int(input('Que tipo de tijolo vocÊ irá usar?\n [1] 9 furos\n [2] 12 furos?\n'))

if tipo_tijolo==1:
    tijolo_9=(24*14)/100
    tijolo_total=parede/tijolo_9
    print(f'Você vai precisar de {tijolo_total} tijolos para construi-lá.')
elif tipo_tijolo==2:
    tijolo_12=(19*19)/100
    tijolo_total=parede/tijolo_12
    print(f'Você vai precisar de {tijolo_total} tijolos para construi-la.')
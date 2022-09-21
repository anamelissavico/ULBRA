numeroDiarias= int(input('Quantas diárias?'))
valor_total = numeroDiarias * 50
if numeroDiarias < 15:
    valor_total += 1.50 * numeroDiarias
    print(valor_total)
elif numeroDiarias == 15:
    valor_total += 1 * numeroDiarias
    print(valor_total)
else:
    valor_total += 0.50 * numeroDiarias
    print(valor_total)

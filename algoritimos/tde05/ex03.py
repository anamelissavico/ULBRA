indice=float(input('Qual o índice de polouição'))
if indice >=0.05 and indice <= 0.25:
    print(f"Índice de poluição aceitável.")
if indice >0.25 and indice <= 0.30:
    print(f"As indústrias do primeiro grupo são intimadas a suspenderem suas atividades.")
if indice >0.30 and indice <= 0.40:
    print(f"As indústrias do primeiro e segundo grupo são intimadas a suspenderem suas atividades.")
if indice >0.40 and indice < 0.50:
    print(f"As indústrias do primeiro,segundo e terceiro grupos devem ser notificados a paralisarem suas atividades.")
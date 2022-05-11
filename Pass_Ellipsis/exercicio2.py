horario = input("Digite as horas")

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Digite um horário entre 00 as 23")
    else:
        if horario <= 11 and horario >= 6:
            print("Bom dia")
        elif horario >= 12 and horario <= 18:
            print("Boa tarde")
        elif horario >= 19  and horario <= 0:
            print("Boa noite")
        elif horario >= 0 and horario <= 5:
            print("Boa madrugada")


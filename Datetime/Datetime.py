import datetime  # módulo para trabalhar com datas

dia_hoje = datetime.datetime.today()  # módulo datetime, função datetime(mostra as horas) e função today(data de hoje)
print(dia_hoje)
print(datetime.datetime.today().date())  # Especifica que só quer a data
print(datetime.datetime.today().time())  # # Especifica que só quer as horas
""" Extraindo data abaixo"""
Data = datetime.datetime.today().date()
Ano = Data.year
Mes = Data.month
Dia = Data.day


print(Dia, Mes, Ano, sep="/")
"""Criando uma data"""

Data_antiga = datetime.date(2021, 4, 11)
print(Data_antiga)

""" Calculo entre datas"""

Data_Delta = Data - Data_antiga

print(Data_Delta)

n = Data + datetime.timedelta(days=100)

print(n)

"""Mudando o formato da data"""
Data_formato = Data.strftime('%d/%m/%y')
print(Data_formato)


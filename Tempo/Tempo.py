import time
"""Bom usar para web scrapping"""
print('Aguarde 1 segundos')
time.sleep(1)
print("Pronto")

Agora = time.localtime()
print(Agora, type(Agora))

print(time.strftime('%d/%m/%y', Agora))
print(time.strftime('%d/%m/%y, %H:%M: %S', Agora))

"""Conversão"""
Time_texto = '21 June, 2021'
time.strptime(Time_texto, '%d %B, %Y')

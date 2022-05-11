"""
operadores relacionais
== igual
> Maior
>= Maior ou igual
<= Menor ou igual
!= Diferente
"""

nome = input("Qual seu nome? ")
idade = input("Qual idade? ")

idade_minima= "18"
idade_maxima = "40"

if idade >= idade_minima and idade <= idade_maxima:
    print("Empréstimo liberado!!!")
else:
    print("Empréstimo não aprovado")





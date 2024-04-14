"""Faça um algoritmo que leia um valor e escreva uma mensagem dizendo em qual dos seguintes intervalos
 ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
Caso o valor não esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”."""

valor = int(input("Digite um valor: "))
if valor >= 0 and valor <= 25:
    print("Intervalo de [0,25]")
elif valor > 25 and valor <= 50:
    print("Intervalo de (25,50]")
elif valor > 50 and valor <=75:
    print('Intervalo de (50 a 70]')
elif valor > 75 and valor <= 100:
    print('Intervalo de (75 a 100]')
else:
    print('Invalido')
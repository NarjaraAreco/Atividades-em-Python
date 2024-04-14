''' Escreva um programa que leia a velocidade de um carro em km/h 
e calcule a multa que o motorista deve pagar, considerando que a multa é de 130,00 mais 5,00 por km/h acima do limite de velocidade de 80km/h.
'''
velocidade = float(input("Digite a velocidade "))

if velocidade == 80:
    print("Multa de 130,00")
elif velocidade > 80:
    velocidade = velocidade - 80
    multa = 130 + (velocidade * 5)
    print(f"Multa de R${multa:.2f}")
else:
    print("Sem multa")

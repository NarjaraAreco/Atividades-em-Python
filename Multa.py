velocidade = float(input("Digite a velocidade "))

if velocidade == 80:
    print("Multa de 130,00")
elif velocidade > 80:
    velocidade = velocidade - 80
    multa = 130 + (velocidade * 5)
    print(f"Multa de R${multa:.2f}")
else:
    print("Sem multa")

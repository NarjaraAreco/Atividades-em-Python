nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))
faltas = float(input("Digite quantas faltas teve: "))

media = (nota1 + (nota2 * 2) + (nota3 * 3) + (nota4 * 4)) / (4 + 3 + 2 + 1)
# print(media)
if media >= 6 and media <= 10 and faltas <= 25.7:
    print("Aprovado")
    print(f"Media = {media:.2f}")
    print(f"Faltas = {faltas:.0f}")
elif media <= 6 and media >= 0 and faltas >= 25.7:
    print("Reprovado")
    print(f"Media = {media:.2f}")
    print(f"Faltas = {faltas:.0f}")
else:
    print("Inválido")

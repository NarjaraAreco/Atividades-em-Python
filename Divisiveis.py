num = int(input("Digite um número: "))
verificacao1 = num % 3
verificacao2 = num % 5

if verificacao1 == 0 and verificacao2 == 0:
    print("Pelos dois")
    print(f"{num} / 3 = {num/3}")
    print(f"{num} / 5 = {num/5}")
elif verificacao1 == 0:
    print("Por 3")
    print(f"{num} / 3 = {num/3}")
elif verificacao2 == 0:
    print("Por 5")
    print(f"{num} / 5 = {num/5}")
else:
    print("Nenhum")

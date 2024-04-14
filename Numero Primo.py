"""Leia um número e verifique se ele é primo."""
#Falta acrescentar numeros como 11*11, 13*13
try:
    numero = int(input("Digite um numero de 0 a 100: "))
    condicao = True if numero < 100 else False
except:
    print('Erro')
else:   
# Erastotenes
    if condicao:
        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            print("Primo")
        elif numero % 2 == 0 and numero > 1:
            print("Não primo pares")
        elif numero % 3 == 0 and numero > 1:
            print("Não primo por 3")
        elif numero % 5 == 0 and numero > 1:
            print("Não primo por 5")
        elif numero % 7 == 0 and numero > 1:
            print("Não primo por 7")
        else:
            print("Primo")
    else:
        print('Por favor um numero menor que 100')
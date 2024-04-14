#Lleia 3 lados de um triângulo e verifique, caso formem um triângulo, se é triângulo escaleno, isósceles ou equilátero.

x = int(input())
y = int(input())
p = int(input())

if (x + y) > p and (x + p) > y and (y + p) > x:
    if x == y == p:
        print("Equilátero")
    elif x == y or x == p or y == p:
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("Não é triangulo")

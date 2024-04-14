""" Leia um par de valores (x, y) do plano cartesiano. 
Determine se o ponto está em um dos quadrantes ou se está sobre um dos eixos cartesianos."""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if x > 0 and y > 0:
    print("1")
elif x > 0 and y < 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x < 0 and y > 0:
    print("4")
else:
    print("Eixos")

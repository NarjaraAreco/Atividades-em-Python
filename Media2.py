""" Leia 2 notas, calcule a media e escreva o resultado de acordo com a tabele: 
(8,0 - 100] - A 
(7,0 - 8,0] - B 
(6,0 - 7,0] - C 
Abaixo de 6,0 - D
"""

nota1 = float(input("Nota 1 = "))
nota2 = float(input("Nota 2 = "))
media = (nota1 + nota2) / 2
if media > 8 and media <= 10:
    print(media)
    print("A")
elif media <= 8 and media > 7:
    print(media)
    print("B")
elif media <= 7 and media >= 6:
    print(media)
    print("C")
elif media < 6 and media >= 0:
    print(media)
    print("D")
else:
    print(media)
    print("Invalido")

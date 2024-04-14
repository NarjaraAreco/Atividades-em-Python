"""Leia uma frase e escreva a frase com as palavras que tiverem 5 ou mais caracteres invertidas. 
Exemplo: Entrada: Hoje teremos aula de comando de seleção. 
Saída esperada: Hoje someret aula de odnamoc de oãçeles
"""

frase = input().split(" ")
fraseCompleta = ""
# print(type(frase))
for i in range(len(frase)):
    # for i in frase:
    if len(frase[i]) > 5:
        palavra = frase[i]
        fraseCompleta = fraseCompleta + " " + palavra[::-1]
    else:
        fraseCompleta = fraseCompleta + " " + frase[i]

print(fraseCompleta.strip())

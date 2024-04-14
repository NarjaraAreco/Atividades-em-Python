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

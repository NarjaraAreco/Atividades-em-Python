email = input("Digite seu email: ")
# emailArroba =
if (email.find("@") == -1) or (email.find(".") == -1):
    print("Invalido, 1")
elif email[::-1].find(".") < email[::-1].find("@"):
    print(email[::-1].find("@"))
    print(email[::-1].find("."))
    print("Verdadeiro")
else:
    print(email[::-1].find("@"))
    print(email[::-1].find("."))
    print("Invalido, 2")

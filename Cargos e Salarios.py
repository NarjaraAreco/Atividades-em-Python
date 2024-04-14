"""Os funcionários da empresa Passarinho receberam um aumento de salário: Técnicos: 50%, Gerentes: 30%, Demais: 20%. 
Faça um algoritmo que leia o salário atual e o cargo do funcionário, e escreva o novo salário após o aumento."""

salario = float(input("Digite seu salário: "))
cargo = input("Digite seu cargo: ")

cargo = cargo.capitalize()

if cargo == "Técnico" or cargo == "Tecnico":
    print(
        f"Seu cargo é Técnico e seu salário novo sera R${salario + (salario*0.5):.2f}"
    )
elif cargo == "Gerente":
    print(
        f"Seu cargo é Gerente e seu salário novo sera R${salario + (salario*0.3):.2f}"
    )
else:
    print(f"Seu salário novo sera R${salario + (salario*0.2):.2f}")

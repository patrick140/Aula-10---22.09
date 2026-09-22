def calc_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

controlador = 1

while controlador == 1:
    peso = float(input("digite o seu peso(use ponto e não virgula): "))
    altura = float(input("digite a sua altura(use ponto e não virgula):"))
    print("\n")

    if calc_imc(peso, altura) > 40:
        print("Você esta com obesidade de grau III\n")
    elif calc_imc(peso, altura) <= 40 and calc_imc(peso, altura) >= 35:
        print("Você esta com obesidade de grau II\n")
    elif calc_imc(peso, altura) <= 34.9 and calc_imc(peso, altura) >= 30:
        print("Você esta com obesidade de grau I\n")
    elif calc_imc(peso, altura) <= 29.9 and calc_imc(peso, altura) >= 25:
        print("Você esta Acima do peso\n")
    elif calc_imc(peso, altura) <= 24.9 and calc_imc(peso, altura) >= 18.5:
        print("Você esta com peso normal\n")
    elif calc_imc(peso, altura) <= 18.4 and calc_imc(peso, altura) >= 17:
        print("Você esta abaixo do peso\n")
    else:
        print("Você esta muito abaixo do peso \n")
    print("Você deseja testar mais alguem? \n Digite 1 para sim e 0 para não")
    controlador = int(input(""))

print("Fim do programa")
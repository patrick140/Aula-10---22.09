def calc_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc > 40:
            print("Você esta com obesidade de grau III\n")
    elif imc <= 40 and imc >= 35:
            print("Você esta com obesidade de grau II\n")
    elif imc <= 34.9 and imc >= 30:
            print("Você esta com obesidade de grau I\n")
    elif imc <= 29.9 and imc >= 25:
            print("Você esta Acima do peso\n")
    elif imc <= 24.9 and imc >= 18.5:
            print("Você esta com peso normal\n")
    elif imc <= 18.4 and imc >= 17:
            print("Você esta abaixo do peso\n")
    else:
            print("Você esta muito abaixo do peso \n")
    return imc

controlador = 1

while controlador == 1:
    peso = float(input("digite o seu peso(use ponto e não virgula): "))
    altura = float(input("digite a sua altura(use ponto e não virgula):"))
    print("\n")
    calc_imc(peso, altura)
    print("Você deseja testar mais alguem? \nDigite 1 para sim e 0 para não")
    controlador = int(input(""))

print("Fim do programa")
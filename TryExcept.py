
try:
    numero = float(input("Digite um numero: "))
except(Exception):
    print("Erro; Numero não digitado!")
else:
    print(f"Você digitou o numero: {numero}")
finally:
    print("Fim do programa")
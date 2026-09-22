Total_peso = float(input("Digite o peso total dos peixes pescados neste dia (somente o peso): "))

def calc_multa(valor):
    limite = 100
    multa = 4.00
    if Total_peso > limite:
        excesso = Total_peso - limite
        multa = excesso * multa
        return multa
    else:
        return 0

multa_peso = calc_multa(Total_peso)

if multa_peso != 0:
    print(f"multa de R${multa_peso:.2f}!") #:.2f faz com que so apareca as duas primeiras casas apos o ponto (virgula)
else:
    print("Valor não excedeu limite e nã gerou multa.")

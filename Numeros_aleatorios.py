import random

def gerar_dados(qtd, min_val, max_val):
    lista = []
    for _ in range(qtd):
        lista.append(random.randint(min_val, max_val))
    return lista

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

dados = gerar_dados(10, 1, 20)
print("Lista de números gerados:", dados)

total_soma = 0
for numero in dados:
    total_soma = soma(total_soma, numero)
print("Soma de todos os números:", total_soma)

total_sub = dados[0]
for i in range(1, len(dados)):
    total_sub = subtracao(total_sub, dados[i])
print("Subtração de todos os números:", total_sub)

total_mult = 1
for numero in dados:
    total_mult = multiplicacao(total_mult, numero)
print("Multiplicação de todos os números:", total_mult)

total_div = dados[0]
for i in range(1, len(dados)):
    total_div = divisao(total_div, dados[i])
print("Divisão de todos os números:", total_div)
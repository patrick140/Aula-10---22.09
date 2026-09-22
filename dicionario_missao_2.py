funcionarios = []

for i in range(5):
    funcionarios.append({"idade": int(input("Digite a idade do candidato: "))})
    if funcionarios[i]["idade"] >= 18:
        funcionarios[i].update({"nome": input("Digite o seu nome: ")})
        funcionarios[i].update({"nascimento": input("Digite a data de nascimento do candidato: ")})
        funcionarios[i].update({"telefone": input("Digite o telefone do candidato: ")})
        funcionarios[i].update({"email": input("Digite o Email do condidato: ")})
        funcionarios[i].update({"Formação": input("Digite a formação do candidato: ")})
        print("\n")
    else:
        print("Candidato menor de idade, não aprovado para contrato.\n")

print("Candidatos: \n")

for i in range(len(funcionarios)): #len()retorna a quantidade de itens em um objeto
    if "nome" in funcionarios[i]: #in em um if testa se um item esta em outro neste caso esta testando se a chave "nome" esta no dicionario que esta dentro da lista
        print("nome do candidato: ", funcionarios[i]["nome"])
        print("Data de nascimento do candidato: ", funcionarios[i]["nascimento"])
        print("Telefone do candidato: ", funcionarios[i]["telefone"])
        print("Email do candidato: ", funcionarios[i]["email"])
        print("Formação do candidato: ", funcionarios[i]["Formação"])
        print("\n")



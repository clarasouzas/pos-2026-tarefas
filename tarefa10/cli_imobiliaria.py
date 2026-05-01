import json

with open("tarefa10/imobiliaria.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

imoveis = dados["imobiliaria"]["imovel"]

print("---IMÓVEIS---")
for i in range(len(imoveis)):
    print(i + 1, "-", imoveis[i]["descricao"])

opcao = int(input("Digite o id do imóvel para saber mais: "))

if 1 <= opcao <= len(imoveis):
    imovel = imoveis[opcao - 1]

    print("\nDescrição:", imovel["descricao"])

    print("\nProprietário:")
    print("Nome:", imovel["proprietario"].get("nome"))

    tel = imovel["proprietario"].get("telefone")
    if isinstance(tel, list):
        print("Telefones:")
        for t in tel:
            print(" ", t)
    else:
        print("Telefone:", tel)

    print("Email:", imovel["proprietario"].get("email"))

    print("\nEndereço:")
    print("Rua:", imovel["endereco"].get("rua"))
    print("Número:", imovel["endereco"].get("número"))
    print("Bairro:", imovel["endereco"].get("bairro"))
    print("Cidade:", imovel["endereco"].get("cidade"))

    print("\nCaracterísticas:")
    print("Tamanho:", imovel["caracteristicas"].get("tamanho"))
    print("Quartos:", imovel["caracteristicas"].get("numQuartos"))
    print("Banheiros:", imovel["caracteristicas"].get("numBanheiros"))

    print("\nValor: R$", imovel["valor"])

else:
    print("ID inválido.")
from xml.dom.minidom import parse
import json

dom = parse("tarefa09/imobiliaria.xml")

raiz = dom.documentElement

# pegar imóveis
imoveis_xml = raiz.getElementsByTagName("imovel")

lista_imoveis = []

for imovel in imoveis_xml:

    # -------- DESCRIÇÃO --------
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    # -------- PROPRIETÁRIO --------
    prop = imovel.getElementsByTagName("proprietario")[0]

    nome = prop.getElementsByTagName("nome")[0].firstChild.nodeValue

    telefones_xml = prop.getElementsByTagName("telefone")
    telefones = []
    for tel in telefones_xml:
        telefones.append(tel.firstChild.nodeValue)

    email = None
    if prop.getElementsByTagName("email"):
        email = prop.getElementsByTagName("email")[0].firstChild.nodeValue

    proprietario = {"nome": nome}

    if telefones:
        if len(telefones) == 1:
            proprietario["telefone"] = telefones[0]
        else:
            proprietario["telefone"] = telefones

    if email:
        proprietario["email"] = email

    # -------- ENDEREÇO --------
    end = imovel.getElementsByTagName("endereco")[0]

    endereco = {
        "rua": end.getElementsByTagName("rua")[0].firstChild.nodeValue,
        "bairro": end.getElementsByTagName("bairro")[0].firstChild.nodeValue,
        "cidade": end.getElementsByTagName("cidade")[0].firstChild.nodeValue
    }

    if end.getElementsByTagName("número"):
        numero = end.getElementsByTagName("número")[0].firstChild.nodeValue
        endereco["número"] = int(numero)

    # -------- CARACTERÍSTICAS --------
    car = imovel.getElementsByTagName("caracteristicas")[0]

    tamanho_texto = car.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    tamanho = int(tamanho_texto.replace("m²", ""))

    caracteristicas = {
        "tamanho": tamanho,
        "numQuartos": int(car.getElementsByTagName("numQuartos")[0].firstChild.nodeValue),
        "numBanheiros": int(car.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue)
    }

    # -------- VALOR --------
    valor = int(imovel.getElementsByTagName("valor")[0].firstChild.nodeValue)

    # -------- JUNTA TUDO --------
    imovel_dict = {
        "descricao": descricao,
        "proprietario": proprietario,
        "endereco": endereco,
        "caracteristicas": caracteristicas,
        "valor": valor
    }

    lista_imoveis.append(imovel_dict)

# -------- ESTRUTURA FINAL --------
saida = {
    "imobiliaria": {
        "imovel": lista_imoveis
    }
}

with open("tarefa09/imobiliaria.json", "w", encoding="utf-8") as arquivo:
    json.dump(saida, arquivo, indent=4, ensure_ascii=False)

print("Arquivo imobiliaria.json criado!")
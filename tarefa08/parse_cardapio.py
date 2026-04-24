from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

id_prato = 0

for prato in pratos:
    id_prato += 1
    nome = prato.getAttribute('nome')
    print(f'{id_prato} - {nome}')
 
    

id_lido = int(input("Digite o id do prato para saber mais: "))
prato = prato[id_lido-1]
print("---\n")

descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
tempoPreparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
ingredientes = prato.getElementsByTagName('ingredientes')[0].firstChild.nodeValue
for ingrediente in ingredientes:
    ingrediente = prato.ingredientes.getElementsByTagName('ingrediente')[0].firstChild.nodeValue
    print(f'Ingredientes - {ingrediente}')
 


print("Descrição:", descricao)
print("Preço:", preco)
print("Calorias:", calorias)
print("Tempo de Preparo:", tempoPreparo)

    
import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

print("\n========== MENU ==========")
print("1 - Código de Telefone")
print("2 - Capital do País")
print("3 - Nome do País")


op = input("Digite a opção: ")

if op == "1":
    operacao = "CountryIntPhoneCode"
elif op == "2":
    operacao = "CapitalCity"
elif op == "3":
    operacao = "CountryName"
else:
    print("Opção invalida")

country_code = input("Digite o código do país: ").upper()

# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <{operacao} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </{operacao}>
                </soap:Body>
            </soap:Envelope>"""
# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
if response.status_code == 200:
    if op == "1":
        print("O código telefônico do país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)
    elif op == "2":
        print("A capital desse país é " + parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)
    elif op == "3":
        print("O nome desse país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)
else:
    print ("Erro")


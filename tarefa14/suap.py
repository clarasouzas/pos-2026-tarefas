import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username":user,"password":password}

response = requests.post(api_url+"token/pair", json=data)
token = response.json()["access"]
headers = {
    "Authorization": f'Bearer {token}'
}
ano = input("Digite o ano: ")
periodo = input("Digite o período: ")
response = requests.get(api_url+ f"ensino/meu-boletim/{ano}/{periodo}", headers=headers)

disciplinas = response.json()["results"]
print("-" * 100)
print(f'{"Disciplina":<70} | {"N1":^5} | {"N2":^5} | {"N3":^5} | {"N4":^5}')
print("-" * 100)
for disciplina in disciplinas:
    print(
        f'{disciplina["disciplina"]:<70} |'
        f'{str(disciplina["nota_etapa_1"]["nota"]):^5} |'
        f'{str(disciplina["nota_etapa_2"]["nota"]):^5} |'
        f'{str(disciplina["nota_etapa_3"]["nota"]):^5} |'
        f'{str(disciplina["nota_etapa_4"]["nota"]):^5} |'
    )
print("-" * 100)

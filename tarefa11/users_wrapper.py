import requests

API_URL = "https://jsonplaceholder.typicode.com"

def listar():
    response = requests.get(f"{API_URL}/users/")

    if response.status_code == 200:
        return response.json()
    
    return False


def criar(dados):
    response = requests.post(f"{API_URL}/users/", json=dados)

    if response.status_code == 201:
        return response.json()
    
    return False


def detalhar(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}/")

    if response.status_code == 200:
        return response.json()
    
    return False


def editar(user_id, dados):
    response = requests.put(f"{API_URL}/users/{user_id}/", json=dados)

    if response.status_code == 200:
        return response.json()
    
    return False


def deletar(user_id):
    response = requests.delete(f"{API_URL}/users/{user_id}/")

    if response.status_code == 204:
        return True
    
    return False
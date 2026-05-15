import users_wrapper as u

opcao_valida = True
while opcao_valida:
    print("Menu")
    print ("opcao dkdfcrjkufdcbj")
    opcao = input("Digite a opção desejada:")
    if opcao == 2:
        user_id = input("Digite o id do usuario desejado: ")
        user = u.read(user_id)
        if user:
            print( f"nome : {user['name']}")
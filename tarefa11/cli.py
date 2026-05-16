import users_wrapper as u

opcao_valida = True

while opcao_valida:

    print("\n========== MENU ==========")
    print("1 - Listar usuários")
    print("2 - Detalhar usuário")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":

        users = u.list()

        if users:

            print("\n===== USUÁRIOS =====")

            for user in users:
                print(f"{user['id']} - {user['name']}")

        else:
            print("Erro ao listar usuários")


    elif opcao == "2":

        user_id = input("Digite o ID do usuário: ")

        user = u.read(user_id)

        if user:

            print("\n========== DETALHES ==========")

            print(f"ID: {user['id']}")
            print(f"Nome: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            print(f"Website: {user['website']}")

            print("\n----- ENDEREÇO -----")
            print(f"Rua: {user['address']['street']}")
            print(f"Suite: {user['address']['suite']}")
            print(f"Cidade: {user['address']['city']}")
            print(f"CEP: {user['address']['zipcode']}")
            print(f"Latitude: {user['address']['geo']['lat']}")
            print(f"Longitude: {user['address']['geo']['lng']}")

            print("\n----- EMPRESA -----")
            print(f"Empresa: {user['company']['name']}")
            print(f"CatchPhrase: {user['company']['catchPhrase']}")
            print(f"BS: {user['company']['bs']}")

        else:
            print("Usuário não encontrado")


    elif opcao == "3":

        dados = {
            "name": input("Nome: "),
            "username": input("Username: "),
            "email": input("Email: "),
            "phone": input("Telefone: "),
            "website": input("Website: "),

            "address": {
                "street": input("Rua: "),
                "suite": input("Suite: "),
                "city": input("Cidade: "),
                "zipcode": input("CEP: "),

                "geo": {
                    "lat": input("Latitude: "),
                    "lng": input("Longitude: ")
                }
            },

            "company": {
                "name": input("Empresa: "),
                "catchPhrase": input("CatchPhrase: "),
                "bs": input("BS: ")
            }
        }

        user = u.create(dados)

        if user:
            print("\nUsuário criado com sucesso!")

        else:
            print("Erro ao criar usuário")


    elif opcao == "4":

        user_id = input("Digite o ID do usuário: ")

        dados = {
            "name": input("Novo nome: "),
            "username": input("Novo username: "),
            "email": input("Novo email: "),
            "phone": input("Novo telefone: "),
            "website": input("Novo website: "),

            "address": {
                "street": input("Nova rua: "),
                "suite": input("Nova suite: "),
                "city": input("Nova cidade: "),
                "zipcode": input("Novo CEP: "),

                "geo": {
                    "lat": input("Nova latitude: "),
                    "lng": input("Nova longitude: ")
                }
            },

            "company": {
                "name": input("Nova empresa: "),
                "catchPhrase": input("Nova catchPhrase: "),
                "bs": input("Novo BS: ")
            }
        }

        user = u.update(user_id, dados)

        if user:
            print("\nUsuário atualizado com sucesso!")

        else:
            print("Erro ao atualizar usuário")


    elif opcao == "5":

        user_id = input("Digite o ID do usuário: ")

        resultado = u.delete(user_id)

        if resultado:
            print("Usuário deletado com sucesso!")

        else:
            print("Erro ao deletar usuário")


    elif opcao == "0":

        print("Fim.")
        opcao_valida = False


    else:
        print("Opção inválida!")
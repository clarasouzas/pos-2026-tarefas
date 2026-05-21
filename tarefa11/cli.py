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

        users = u.listar()

        if users:

            print("\n===== USUÁRIOS =====")

            for user in users:
                print(f"{user['id']} - {user['name']}")

        else:
            print("Erro ao listar usuários")


    elif opcao == "2":

        id = input("Digite o ID do usuário: ")

        user = u.detalhar(id)

        if user:

            print("\n========== DETALHES ==========")

            print(f"ID: {user['id']}")
            print(f"Nome: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            print(f"Website: {user['website']}")

        else:
            print("Usuário não encontrado")


    elif opcao == "3":

        dados = {
            "name": input("Nome: "),
            "username": input("Username: "),
            "email": input("Email: "),
            "phone": input("Telefone: "),
            "website": input("Website: ")}


        user = u.criar(dados)

        if user:
            print("\nUsuário criado com sucesso!")

        else:
            print("Erro ao criar usuário")


    elif opcao == "4":

        id = input("Digite o ID do usuário: ")

        dados = {
            "name": input("Novo nome: "),
            "username": input("Novo username: "),
            "email": input("Novo email: "),
            "phone": input("Novo telefone: "),
            "website": input("Novo website: "),}

        user = u.editar(id, dados)

        if user:
            print("\nUsuário atualizado com sucesso!")

        else:
            print("Erro ao atualizar usuário")


    elif opcao == "5":

        id = input("Digite o ID do usuário: ")

        resultado = u.deletar(id)

        if resultado:
            print("Usuário deletado com sucesso!")

        else:
            print("Erro ao deletar usuário")


    elif opcao == "0":

        print("Fim.")
        opcao_valida = False


    else:
        print("Opção inválida!")
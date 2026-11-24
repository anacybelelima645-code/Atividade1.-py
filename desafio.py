
usuarios = []

logado = False
usuario_logado = ""

while True:
    print("\033c", end="") 
    print("#########################################")
    print("SISTEMA DE CADASTRO DE USUÁRIOS")
    print("#########################################\n")

    if not logado:
        print("===LOGIN===")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "admin" and senha == "123":
            print(f"Login realizado com sucesso! Bem-vindo, {login}!\n")
            input("ENTER para continuar...")
            logado = True
            usuario_logado = login
        else:
            input("\nLogin ou senha incorretos! ENTER para tentar novamente.")

    else:
        print("===MENU PRINCIPAL===")
        print(f"Usuário logado: {usuario_logado}")
        print("1 - Inserir usuário")
        print("2 - Pesquisar usuário")
        print("3 - Remover usuário")
        print("4 - Listar todos os usuários")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n=== INSERIR USUÁRIO ===")
            nome = input("Digite o nome do usuário: ")

            if nome.strip() == "":
                print("Nome não pode ficar vazio!")
            elif nome in usuarios:
                print("Este usuário já está cadastrado!")
            else:
                usuarios.append(nome)
                print("Usuário cadastrado com sucesso!")

            input("\nENTER para continuar...")

        elif opcao == "2":
            print("\n=== PESQUISAR USUÁRIO ===")
            nome = input("Digite o nome que deseja pesquisar: ")

            if nome in usuarios:
                print(f"\nUsuário {nome} encontrado!")
            else:
                print("\nUsuário não encontrado!")

            input("\nENTER para continuar...")

        elif opcao == "3":
            print("\n=== REMOVER USUÁRIO ===")
            nome = input("Digite o nome que deseja remover: ")

            if nome in usuarios:
                usuarios.remove(nome)
                print("Usuário removido com sucesso!")
            else:
                print("Usuário não encontrado!")

            input("\nENTER para continuar...")

        elif opcao == "4":
            print("\n=== LISTA DE USUÁRIOS ===")

            if len(usuarios) == 0:
                print("Nenhum usuário cadastrado!")
            else:
                for i, nome in enumerate(usuarios, start=1):
                    print(f"{i} - {nome}")

            input("\nENTER para continuar...")

        elif opcao == "5":
            print("Fazendo logout...")
            input("ENTER para voltar para o login.")
            usuario_logado = ""
            logado = False

        elif opcao == "6":
            print("Encerrando o sistema... Até logo!")
            break

        else:
            input("Opção inválida! ENTER para continuar...")

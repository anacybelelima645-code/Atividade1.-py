import os

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("===== LOGIN =====")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":
        print("Login realizado com sucesso!")
        input("Pressione ENTER para continuar...")

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("===== MENU =====")
            print("1 - Gerenciar usuários")
            print("2 - Logout")
            print("3 - Encerrar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Opção ainda não disponível.")
                input("Pressione ENTER para voltar ao menu...")

            elif opcao == "2":
                print("Fazendo logout...")
                input("Pressione ENTER para continuar...")
                break

            elif opcao == "3":
                print("Programa encerrado!")
                exit()

            else:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")

    else:
        print("Usuário ou senha incorretos!")
        input("Pressione ENTER para tentar novamente...")

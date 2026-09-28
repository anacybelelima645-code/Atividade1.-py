import random
import os

while True:
    print("===== JOGO DE ADIVINHAÇÃO =====")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        limite = 10
    elif nivel == 2:
        limite = 20
    elif nivel == 3:
        limite = 30
    else:
        print("Opção inválida!")
        continue

    numero_sorteado = random.randint(1, limite)
    acertou = False

    for tentativa in range(1, 4):
        numero = int(input(f"Tentativa {tentativa}/3 - Digite um número: "))

        if numero == numero_sorteado:
            print("Parabéns, você acertou!")
            acertou = True
            break
        elif numero < numero_sorteado:
            print("Você errou!")
            print("Tente um número maior")
        else:
            print("Você errou!")
            print("Tente um número menor")

    if not acertou:
        print("Você perdeu! Fim de jogo.")
        print(f"O número sorteado era {numero_sorteado}.")

    novamente = input("Quer jogar novamente? (s/n): ").lower()

    if novamente != "s":
        print("Fim de jogo!")
        break

    os.system("cls" if os.name == "nt" else "clear")

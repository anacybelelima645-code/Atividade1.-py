import random 

lista = []

while True:
  nome = input("Digite o nome dos compradores: ")
  lista.append(nome)
  sorteado = random.choice(lista)
  continuar = input("Deseja colocar mais um nome na lista?(s/n): ").lower()
  
  if continuar == "s":
    continue
  
  elif continuar == "n":
     print(f"O vencedor foi, {sorteado}")
     break

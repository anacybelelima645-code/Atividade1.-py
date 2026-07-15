soma = 0 quantidade = 0 maior = 0

while True: numero = int(input("Digite um número: ")) if numero < 0: break soma += numero quantidade += 1

if quantidade == 1 or numero > maior:
    maior = numero
if quantidade > 0: media = soma / quantidade

print("Resultados")
print(f"Soma é igual a:{soma}")
print(f"Média é igual a:{media}")
print(f"Maior número é: {maior}")
else: print("Nenhum número foi informado!")

print(30*"#")
print("Bem vindo ao jogo de adivinhação")
print(30*"#")

numero_secreto = 43
number = int(input("Digite um número: "))
if(number == numero_secreto):
    print(f"Você acertou o número é {number}!!")
else:
    print("Você errou")

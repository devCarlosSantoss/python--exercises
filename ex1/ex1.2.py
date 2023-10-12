from random import *
print("Jogo da adivinhação")

num = randint(0, 100)
contador = 0
while True:
    num1 = int(input("Digite um número entre 0 e 100: "))
    if(num1 == num):
        print("Você acertou!!")
        break
    else:
        print("Tente novamente!!")
        contador +=1
        if(contador == 10):
            break
    
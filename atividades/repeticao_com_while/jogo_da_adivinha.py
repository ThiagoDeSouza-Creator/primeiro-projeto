import random
numero = random.randint(1, 10)
adivinhacao = 0
while adivinhacao != numero:
    adivinhacao= int(input("Adivinhe o numero que pensei: "))
    if adivinhacao < numero:
        print("Muito baixo,tente denovo!")
    elif adivinhacao > numero:
        print("Muito alto,tente denovo!")
    else:
        print("Voce acertou,muito bem!")
        break
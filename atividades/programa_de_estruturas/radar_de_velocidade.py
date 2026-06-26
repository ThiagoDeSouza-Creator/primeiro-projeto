import random

vel = random.randint(60,120)
print(f"Velocidade igual a: {vel}")

if vel <= 80:
    print("Boa viagem, dirija com cuidade")
else:
    print("limite atingido, aprenda a dirigir")
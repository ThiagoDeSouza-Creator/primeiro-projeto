import random
atleta = random.randint(9, 30)
print(f"{atleta} anos")

if atleta <9:
    print("Mirirm")
elif atleta <14:
    print("Infantil")
elif atleta <19:
    print("Junior")
elif atleta <25:
    print("Sênior")
else:
    print("Master")
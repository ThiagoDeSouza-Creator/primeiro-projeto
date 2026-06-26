import random

temperatura = random.randint(0, 40)
print(f"{temperatura}°C")

if temperatura < 15:
    print("Clima Frio")
elif temperatura < 25:
    print("Clima Agradável")
else:
    print("Clima Quente")
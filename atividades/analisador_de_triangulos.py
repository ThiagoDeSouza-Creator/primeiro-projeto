t1 = float(input("Digite o valor do Lado A: "))
t2 = float(input("Digite o valor do Lado B: "))
t3 = float(input("Digite o valor do Lado C: "))

if t1 + t2 < t3 or t1 + t3 < t2 or t2 + t3 < t1:
    print("Triâgulo Inválido")
else:
    if t1 == t2 and t1 == t3 and t2 == t3:
        print("Triângulo Equilátero")
    elif t1 != t2 and t1 != t3 and t2 != t3:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
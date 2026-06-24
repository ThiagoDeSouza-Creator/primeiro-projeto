idade_maior = 0
idade_menor = 0
for i in range(1,8):
    nascimento = int(input(f"Digite o seu ano de nascimento{i}: "))
    idade = 2026 - nascimento
    if idade >= 18:
        idade_maior += 1
    else:
        idade_menor += 1
print(f"Os maiores de idade são {idade_maior} e os menores de idade são {idade_menor}")
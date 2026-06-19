salario = float(input("Digite seu salário: "))
parcela = float(input("Digite o valor da parcela: "))

parcela_max = salario * 0.30

if salario >= parcela_max:
    print("Credito Aprovado")
else:
    print("Credito Recusado")
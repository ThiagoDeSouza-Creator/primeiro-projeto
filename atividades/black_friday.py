valor_crompra = float(input("Informe o valor da compra:"))

if valor_crompra <= 100:
    print(f"Sua compra foi de R${valor_crompra} e você não teve desconto")
elif valor_crompra <= 300:
    desconto = valor_crompra * 0.5
    valor_final = valor_crompra - desconto
    print(f"Sua compra foi de R${valor_crompra} pois você teve um desconmto de R${desconto} e o seu pagamento final será de R${valor_final}")
elif valor_crompra <= 500:
    desconto = valor_crompra * 0.1
    valor_final = valor_crompra - desconto
    print(f"Sua compra foi de R${valor_crompra} pois você teve um desconmto de R${desconto} e o seu pagamento final será de R${valor_final}")
else:
    desconto = valor_crompra * 0.15
    valor_final = valor_crompra - desconto
    print(f"Sua compra foi de R${valor_crompra} pois você teve um desconmto de R${desconto} e o seu pagamento final será de R${valor_final}")
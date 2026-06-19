usuario = input("Digite seu nome: ")

ano = int(input(f"\n Digite o ano de nascimento: "))
idade = 2026 - ano

if idade >= 16:
    print("Acesso Liberado")
else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos")
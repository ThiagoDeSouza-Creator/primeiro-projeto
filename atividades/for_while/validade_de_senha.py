senha_correta = "080522"

for tentativa in range(1, 4):
    senha_digitada = input(f"Tentativa {tentativa}/3 - Digite sua senha: ")

    if senha_digitada == senha_correta:
        print("WIN")
        break
else:
    print("FATALITY")
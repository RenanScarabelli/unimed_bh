saldo = 2500
limite = 1000
opcao = -1

saque = float(input("Informe o valor para saque: "))

if saque <= saldo:
    saldo_final = saldo - saque
    print("Saque realizado com sucesso.")
    print(f"Saldo atual é: {saldo_final:.2f}")
    saldo = saldo_final

elif saque <= saldo + limite:
    #Usando as aspas triplas para criar um menu mais fácil
    opcao = int(input("""
    
    Saldo insuficiente, deseja utilizar seu limite?
    
    [1] Sim
    [2] Não
    """))
    
    if opcao == 1:
        saldo_final = saldo - saque
        print("Saque realizado com sucesso.")
        print(f"Saldo atual é: {saldo_final:.2f}")
        saldo = saldo_final
    else:
        print("Saque não realizado")
elif saque >= saldo + limite:
    print("Saldo + Limite insuficiente.")

print("Fim da operação.")
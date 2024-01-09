menu = """

[1]Deposito
[2]Saque
[3]Extrato
[0]Sair

=>>"""

saldo = 0
limite = 500
extrato = ""
qnt_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == '1':
        print("===Opção 1 - Depósito===")
        deposito = float(input("Digite o valor do depósito: R$"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito no valor de R${deposito:.2f}\n"
            print(extrato)
        else:
            print("Valor inválido.")
            
    elif opcao == '2':
        print("===Opção 2 - Saque===")
        saque = float(input("Informe o valor do saque: R$"))
        if saque > saldo:
            print(f"Saldo insuficiente. Saldo atual: R${saldo:.2f}")
        elif saque > limite:
            print("Valor maior que limite. Favor inserir um valor válido.")
        elif qnt_saques >= LIMITE_SAQUE:
            print("Quantidade maxima de saques atingida. Procure seu gerente.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            qnt_saques += 1
            print(extrato, "\nSaques disponíveis: ", (LIMITE_SAQUE - qnt_saques))
        else:
            print("Valor inválido.")
            
    elif opcao == '3':
        print("\n============================Extrato============================")
        print("Sem movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================================")

    elif opcao == '0':
        print("Obrigado!!")
        break
    
    else:
        print("Digite uma opção válida.")


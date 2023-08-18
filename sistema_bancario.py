limite_valor_saque = 500 ## 500 no maximo por saque
limite_diario_saque = 0 ## 3 saques diarios no maximo
saldo = 0
extrato = ""

menu = """

### BANCO DIO - CAIXA ELETRONICO ###

        [d] - Depósitos
        [s] - Saques
        [e] - Extratos
        [q] - Sair do Sistema

"""
while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso, retire o comprovante.")
            
        else:
            print("Falha na Operação, Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Falha na Operação, Saldo insuficiente.")
        elif valor > limite_valor_saque or valor <= 0:
            print("Falha na Operação, Valor de saque não permitido.")
        elif limite_diario_saque >= 3:
            print("Falha na Operação, Limite diário de saque atingido.")
        
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            limite_diario_saque += 1
            print("Saque realizado com sucesso, retire o dinheiro.")
            
    elif opcao == "e":
        print ("\n##########  EXTRATO ##########")
        if not extrato:
            print ("\nNão houve movimentação")  
            print ("\n##############################")
        else:
            print(extrato)
            print (f"\nSaldo: R$ {saldo:.2f}")
            print ("\n##############################")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços.")
        break

    else:
        print("Opção inválida. Verifique e tecle novamente.")


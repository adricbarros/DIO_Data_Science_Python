import textwrap


def menu(): 
    menu = """\n

    =========== MENU ===========

        [d] - Depósitos
        [s] - Saques
        [e] - Extratos
        [u] - Cadastro Usuarios
        [c] - Cadastro Contas
        [l] - Listar Contas
        [q] - Sair do Sistema
        => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso, retire o comprovante.")
    else:
            print("\nFalha na Operação, Valor informado é inválido.")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite_valor_saque, limite_diario_saque):
    if valor > saldo:
            print("\nFalha na Operação, Saldo insuficiente.")
    elif valor > limite_valor_saque or valor <= 0:
            print("\nFalha na Operação, Valor de saque não permitido.")
    elif limite_diario_saque >= 3:
            print("\nFalha na Operação, Limite diário de saque atingido.")
    else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            limite_diario_saque += 1
            print("\nSaque realizado com sucesso, retire o dinheiro.")

    return saldo, extrato, limite_diario_saque


def exibir_extrato(saldo, /, *, extrato):
       print ("\n==========  EXTRATO ==========")
       if not extrato:
            print ("\nNão houve movimentação")  
            print ("\n==============================")
       else:
            print(extrato)
            print (f"\nSaldo: R$ {saldo:.2f}")
            print ("\n===============================")


def criar_usuario(usuarios):
     cpf = input("Informe o CPF do Cliente (Somente Números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
        print("\nUsuário já cadastrado com esse CPF !")
        return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
     endereco = input("Informe o endereço (Logradouro, nº - Bairro - Cidade-UF): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

     print("\n=== Usuário cadastrado com Sucesso ! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, operação cancelada!")
      

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    
    AGENCIA = "0001"

    numero_conta = 0
    saldo = 0
    limite_valor_saque = 500 ## 500 no maximo por saque
    limite_diario_saque = 0 ## 3 saques diarios no maximo
    extrato = ""
    usuarios =[]
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
             
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, limite_diario_saque = sacar(
                 saldo=saldo,
                 valor=valor,
                 extrato=extrato,
                 limite_diario_saque=limite_diario_saque,
                 limite_valor_saque=limite_valor_saque,
            )
           
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "l":
             listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por utilizar nossos servicos.")
            break
    
        else:
            print("\nOpção inválida. Verifique e tecle novamente.")

main()
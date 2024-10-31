menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == "2":
        if numero_de_saques < LIMITE_DE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if valor > limite:
                print(f'O valor máximo para saque é R$ {limite:.2f}.')
            elif valor > saldo:
                print('Saldo insuficiente para realizar o saque.')
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Limite de saques diários atingido.')

    elif opcao == "3":
        print("\n--- Extrato ---")
        print(f'Saldo atual: R$ {saldo:.2f}')
        if extrato == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print('-------------------\n')

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

        
        



menu = """
**************MENU**************
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor informado inválido!")
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Saldo insuficente!")
        elif valor > limite:
            print("Limite para saque insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor informado é inválido!")
    elif opcao == "2":
        print("**************EXTRATO**************")
        if extrato == "":
            print("Sem movimentação no dia.\n")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("***********************************")
    elif opcao == "3":
        break
    else:
        print("Operação inválida, por favor escolha uma opção válida.")

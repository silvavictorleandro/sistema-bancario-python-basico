menu = """
Informe a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

"""

saldo = 0
numero_saques = 0
LIMITE_QUANTIDADE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
extrato = ""


while True:
    pergunta_inicial = int(input(f"{menu}"))

    if pergunta_inicial == 1:
        valor_deposito = float(input("\nDigite o valor que deseja depositar: \n\n"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
            print("\nDeseja mais alguma coisa?")
        else:
            print("\nValor inválido para depósito! Digite novamente:\n")

    elif pergunta_inicial == 2:
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque <= LIMITE_VALOR_SAQUE:
            if valor_saque <= saldo:
                if numero_saques < LIMITE_QUANTIDADE_SAQUES:
                    numero_saques += 1
                    saldo -= valor_saque
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
                    print("\nDeseja mais alguma coisa?")
                else:
                    print("\nLimite de saques diário atingido.")
                    print("\nSão permitidos apenas 3 saques diários.")
                    print("\nDeseja mais alguma coisa?")                    
            else:
                print("\nSaldo insuficiente! Verifique o saldo atual e tente novamente")
        else:
            print("\nValor inválido! Só é possível saque de até R$ 500,00")

    elif pergunta_inicial == 3:
        print("============== EXTRATO ==============")
        print(f"{extrato}")
        print(f"{saldo:.2f}")
        print("=====================================")
        print("\nDeseja mais alguma coisa?")

    elif pergunta_inicial == 0:
        print("\nAgradecemos o contato!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

import textwrap


def menu():
    menu = """\n
    ============ MENU ============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print(f"\n=== Depósito de R$ {valor_deposito:.2f} realizado com sucesso! ===")

    else:
        print("\n@@@ Valor inválido para depósito! @@@\n")

    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_quantidade_saques):

    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_quantidade_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente! @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite de R$ 500,00 @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedidos! @@@")
        
    elif valor_saque <= saldo:
        saldo -= valor_saque
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido! @@@")
    
    return saldo, extrato


def exibir_extratos(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=============================")


def main():
    LIMITE_QUANTIDADE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        pergunta_inicial = menu()

        if pergunta_inicial == "1":
            valor_deposito = float(input("\nDigite o valor que deseja depositar: \n\n"))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)            

        elif pergunta_inicial == "2":
            valor_saque = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_quantidade_saques=LIMITE_QUANTIDADE_SAQUES
            )            

        elif pergunta_inicial == "3":
            exibir_extratos(saldo, extrato=extrato)

        elif pergunta_inicial == "0":
            print("\nAgradecemos o contato!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
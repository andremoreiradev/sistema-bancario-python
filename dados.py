import sys

# Inicialize o saldo da conta em 0
saldo = 0

# Crie uma lista para armazenar as operações
operacoes = []

# Leia o nome do usuário
nome = input("Qual é o seu nome? ")

# Loop até que o usuário digite 'q' para sair
while True:

    # Exiba o menu de opções
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver extrato")
    print("4. Sair")

    # Leia a opção do usuário
    escolha = input("O que você gostaria de fazer? ")

    # Se o usuário escolher 'depositar', leia o valor do depósito e adicione-o ao saldo
    if escolha == "1":
        deposito = float(input("Quanto você gostaria de depositar? "))
        if deposito > 0:
            saldo += deposito
            operacoes.append("Depósito de R$ {:.2f}".format(deposito))
        else:
            print("O valor do depósito deve ser positivo.")

    # Se o usuário escolher 'sacar', leia o valor do saque e subtraia-o do saldo
    elif escolha == "2":
        saque = float(input("Quanto você gostaria de sacar? "))
        if saque <= saldo and saque <= 500:
            saldo -= saque
            operacoes.append("Saque de R$ {:.2f}".format(saque))
        else:
            print("O valor do saque é maior que o saldo ou maior que o limite de R$ 500,00.")

    # Se o usuário escolher 'ver extrato', exiba a lista de operações
    elif escolha == "3":
        for operacao in operacoes:
            print(operacao)

    # Se o usuário escolher 'sair', saia do loop
    elif escolha == "4":
        sys.exit()

    # Se o usuário escolher uma opção inválida, exiba uma mensagem de erro
    else:
        print("Opção inválida.")

# Exiba o saldo final da conta
print("Seu saldo atual é R$ {:.2f}".format(saldo))


# regras de negocio
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


def menu():
    print('''
          Menu
          1 - Depósito
          2 - Saque
          3 - Extrato
          0 - Sair
          ''')
    

while True:

    menu()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        print('\nDepósito\n')
        valor_deposito = float(input('Qual quantia deseja depositar: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
            print('Operação realizada com sucesso.')
        else:
            print('Não foi possível concluir a operação. Valor informado é inválido.')

    elif opcao == '2':
        print('\nSaque\n')
        valor_sacado = float(input('Qual quantia deseja sacar: '))
        if valor_sacado > saldo:
            print('Não foi possível concluir a operação. Saldo insuficiente.')
        elif valor_sacado > limite:
            print('Não foi possível concluir a operação. O valor excede o limite de saque.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Não foi possível concluir a operação. Foi atingido o limite de saques diário.')
        elif valor_sacado > 0:
            saldo -= valor_sacado
            extrato += f'Saque: R$ {valor_sacado:.2f}\n'
            numero_saques += 1
            print('Operação realizada com sucesso.')
        else: 
            print('Não foi possível concluir a operação. Valor informado é inválido.')

    elif opcao == '3':
        print('\nExtrato\n')
        if len(extrato) > 0:
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}')
        else:
            print('Não foram realizadas movimentações.')

    elif opcao == '0':
        print('Sistema finalizado.')
        break
    else:
        print('Opção inválida!\nPor favor selecione uma das opções listadas.')
#regras de negocio
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

#menu
def menu():
    print('''
          Menu
          1 - Depósito
          2 - Saque
          3 - Extrato
          4 - Cadastrar Cliente
          5 - Criar Conta Corrente
          0 - Sair
          ''')
    

#funcao depositar
def depositar(saldo, valor, extrato):
    print('\nDepósito\n')
    valor = float(input('Qual quantia deseja depositar: '))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Operação realizada com sucesso.')
    else:
        print('Não foi possível concluir a operação. Valor informado é inválido.')

    '''
    sugestao de retorno
    return saldo, extrato
    '''


#funcao sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    print('\nSaque\n')
    valor = float(input('Qual quantia deseja sacar: '))
    if valor > saldo:
        print('Não foi possível concluir a operação. Saldo insuficiente.')
    elif valor> limite:
        print('Não foi possível concluir a operação. O valor excede o limite de saque.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Não foi possível concluir a operação. Foi atingido o limite de saques diário.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Operação realizada com sucesso.')
    else: 
        print('Não foi possível concluir a operação. Valor informado é inválido.')

    '''
    sugestao de retorno
    return saldo, extrato
    '''


#funcao exibir_extrato
def exibir_extrato(saldo, *, extrato):
    print('\nExtrato\n')
    if len(extrato) > 0:
        print(extrato)
        print(f'Saldo: R$ {saldo:.2f}')
    else:
        print('Não foram realizadas movimentações.')


#funcao cadastrar_cliente
def cadastrar_cliente():
    clientes = {
        'nome' : {},
        'data_nascimento' : {},
        'cpf' : {},
        'endereço': {'logradouro', 'nro', 'bairro', 'cidade_estado'},
    }
    print('funcao em construcao')


#funcao criar_conta
def criar_conta_corrente(agencia='0001', numero_conta, cliente):
    contas = []


    print('funcao em construcao')



while True:

    menu()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        depositar()

    elif opcao == '2':
        sacar()

    elif opcao == '3':
        exibir_extrato()

    elif opcao == '4':
        cadastrar_cliente()

    elif opcao == '5':
        criar_conta_corrente()

    elif opcao == '0':
        print('Sistema finalizado.')
        break

    else:
        print('Opção inválida!\nPor favor selecione uma das opções listadas.')

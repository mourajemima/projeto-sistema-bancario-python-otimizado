def menu():
    print('''
          Menu
          1 - Depósito
          2 - Saque
          3 - Extrato
          4 - Cadastrar Cliente
          5 - Criar Conta Corrente
          6 - Listar Contas
          0 - Sair
          ''')
    
    return input('Escolha uma opção: ')


#funcao depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Operação realizada com sucesso.')
    else:
        print('Não foi possível concluir a operação. Valor informado é inválido.')

    return saldo, extrato


#funcao sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print('Não foi possível concluir a operação. Saldo insuficiente.')
    elif valor> limite:
        print('Não foi possível concluir a operação. O valor excede o limite de saque.')
    elif numero_saques >= limite_saques:
        print('Não foi possível concluir a operação. Foi atingido o limite de saques diário.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Operação realizada com sucesso.')
    else: 
        print('Não foi possível concluir a operação. Valor informado é inválido.')

    return saldo, extrato


#funcao exibir_extrato
def exibir_extrato(saldo, /, *, extrato):
    print('\nExtrato\n')
    if len(extrato) > 0:
        print(extrato)
        print(f'Saldo: R$ {saldo:.2f}')
    else:
        print('Não foram realizadas movimentações.')


#funcao cadastrar_cliente
def cadastrar_cliente(usuarios):
    cpf = input('Digite o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: 
        print('Já existe um usuário com esse CPF')
        return
    
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Cliente cadastro com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


#funcao criar_conta
def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input('Digite o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: 
        print('Conta corrente criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuário não encontrado. Operação encarrada.')

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:

        opcao = menu()
        
        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            cadastrar_cliente(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '0':
            print('Sistema finalizado.')
            break

        else:
            print('Opção inválida!\nPor favor selecione uma das opções listadas.')

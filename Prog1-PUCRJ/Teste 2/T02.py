#    @jxvtrl    #

def mensagem(conta, saldo, saque):
    print('Sua conta é: %s' % conta)
    print('Seu saldo é de: R$%.2f' % saldo)
    print('Valor do saque: R$%.2f' % saque)

    if conta[0] == '8' or conta[0] == '9':
        print('Você acaba de receber R$100.00')
        saldo = saldo + 100

    saldo = saldo - saque

    print('Seu saldo agora é de: R$%.2f' % saldo)

    if saldo < 0:
        print('Alerta: Seu saldo está negativo!')
        if saldo < -5000:
            print('Seu saldo está abaixo do recomendado pelo banco, favor comparecer à agência mais próxima')
    return


conta = input('Digite aqui o número da sua conta: ')
saldo = float(input('Digite aqui seu saldo atual: '))
saque = float(input('Digite aqui o valor que deseja sacar: '))

mensagem(conta, saldo, saque)
input('Aperte ENTER para sair')

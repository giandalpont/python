# coding=utf-8
import getpass
import os

if os.name == 'nt':
    clear = lambda: os.system('nt')
else:
    clear  = lambda: os.system('clear')

while True:

    clear()

    print(' ')
    print("*******************************************")
    print("*********** Caixa Eletrônico  *************")
    print("*******************************************")
    print(' ')


    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    ## print(account_typed)
    ## print(password_typed)

    accounts_list = {
        '0001-02': {
            'agency': '0001-02',
            'password': '01',
            'name': 'João da Silva',
            'value': 100,
        },
        '0002-02': {
            'agency': '0002-02',
            'password': '02',
            'name': 'Maria da Silva',
            'value': 50,
        },
    }

    clear()

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        print('Olá, %s' % accounts_list[account_typed]['name'] + '!')
        print(' ')
        
        print('1 - Saldo')
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            print(' ')
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])

    else:
        print('Conta inválida')

    print(' ')
    input('Precione <ENTER> para continuar...')
    clear()


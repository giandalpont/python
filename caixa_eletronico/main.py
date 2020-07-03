# coding=utf-8
import getpass
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:

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
            'admin': False,
        },
        '0002-02': {
            'agency': '0002-02',
            'password': '02',
            'name': 'Maria da Silva',
            'value': 50,
            'admin': False,
        },
        '1111-11': {
            'password': '1111',
            'name': 'Gerente',
            'value': 0,
            'admin': True,
        }
    }

    money_slips = {
        '20': 5,
        '50': 5,
        '100': 5,
    }

    clear()

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        print('Olá, %s' % accounts_list[account_typed]['name'] + '!')
        print(' ')
        
        if  accounts_list[account_typed]['admin']:
            print('0 - Incluir cédulas')
        
        print('1 - Saldo')
        option_typed = input('Escolha uma das opções acima: ')

        if option_typed == '1':
            print(' ')
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])

        if option_typed == '0' and accounts_list[account_typed]['admin']:
            amount_typed =  input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')

            money_slips[money_bill_typed] += int(amount_typed)
            
            print(money_slips)

    else:
        print('Conta inválida')

    print(' ')
    input('Precione <ENTER> para continuar...')
    clear()

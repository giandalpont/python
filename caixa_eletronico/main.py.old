# coding=utf-8
import getpass
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

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

    clear()

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        print('Olá, %s' % accounts_list[account_typed]['name'] + '!')
        print(' ')
        
        if  accounts_list[account_typed]['admin']:
            print('0 - Incluir cédulas')
        
        print('1 - Saldo')
        print('2 - Saque')
        option_typed = input('Escolha uma das opções acima: ')

        clear()

        if option_typed == '1':
            print(' ')
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])

        if option_typed == '0' and accounts_list[account_typed]['admin']:
            amount_typed =  input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')

            money_slips[money_bill_typed] += int(amount_typed)
            
            print(money_slips)
        
        if option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            value_int = int(value_typed)

            money_slips_user = {}

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100
            
            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50
            
            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('Caixa não tem cédulas disponíves para este valor!')
            else :
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                
                clear()
                print('Retire as notas.')
                print(money_slips_user)


    else:
        print('Conta inválida')

    print(' ')
    input('Precione <ENTER> para continuar...')
    clear()

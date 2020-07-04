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

money_values = (
    100,
    50,
    20,
)

def main():    
    header()

    account_auth = auth_account()
    clear()

    if account_auth:
        option_typed = get_menu_option_typed(account_auth)
        clear()

        do_operation(option_typed, account_auth)

    else:
        print('Conta inválida')

    print(' ')

def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)

    if option_typed == '0' and accounts_list[account_auth]['admin']:
        insert_money_slips()
    
    if option_typed == '2':
        withdrew()

def show_balance(account_auth):
    print('Seu saldo é %s' % accounts_list[account_auth]['value'])

def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')

    money_slips[money_bill_typed] += int(amount_typed)
    
    print(money_slips)

def withdrew():
    value_typed = input('Digite o valor a ser sacado: ')
    value_int = int(value_typed)
    
    money_slips_user = count_money_slips(value_int)['money_slips_user']
    value_int = count_money_slips(value_int)['value_int']
    
    # if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
    #     money_slips_user['50'] = value_int // 50
    #     value_int = value_int - value_int // 50 * 50
    
    # if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
    #     money_slips_user['20'] = value_int // 20
    #     value_int = value_int - value_int // 20 * 20

    if value_int != 0:
        print('Caixa não tem cédulas disponíves para este valor!')
    else :
        for money_bill in money_slips_user:
            money_slips[money_bill] -= money_slips_user[money_bill]
        
        clear()
        print('Retire as notas.')
        print(money_slips_user)

def count_money_slips(value_int):
    money_slips_user = {}

    for value in money_values:
        if value_int // value > 0 and value_int // value <= money_slips[str(value)]:
            money_slips_user[str(value)] = value_int // value
            value_int = value_int - value_int // value * value
     
    return {'money_slips_user': money_slips_user, 'value_int': value_int}

def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False

def get_menu_option_typed(account_auth):
    print('Olá, %s' % accounts_list[account_auth]['name'] + '!')
    print(' ')
    
    if  accounts_list[account_auth]['admin']:
        print('0 - Incluir cédulas')
    
    print('1 - Saldo')
    print('2 - Saque')
    return input('Escolha uma das opções acima: ')

def header():
    print(' ')
    print("*******************************************")
    print("*********** Caixa Eletrônico  *************")
    print("*******************************************")
    print(' ')

while True:
    main()

    input('Precione <ENTER> para continuar...')
    clear()

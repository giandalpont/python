import getpass
from utils import  clear
from data import accounts_list, money_slips, money_values

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

    count_slip = count_money_slips(value_int)
    value_int = count_slip[0]
    money_slips_user = count_slip[1]
    
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
    
    return value_int, money_slips_user

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


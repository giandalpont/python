# coding=utf-8
import utils
from controller import auth_account, get_menu_option_typed, do_operation

def main():    
    utils.header()

    account_auth = auth_account()
    utils.clear()

    if account_auth:
        option_typed = get_menu_option_typed(account_auth)
        utils.clear()

        do_operation(option_typed, account_auth)

    else:
        print('Conta inválida')

    print(' ')

while True:
    main()

    input('Precione <ENTER> para continuar...')
    utils.clear()

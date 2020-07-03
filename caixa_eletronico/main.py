# coding=utf-8

print(' ')
print("*******************************************")
print("*********** Caixa Eletrônico  *************")
print("*******************************************")
print(' ')

import getpass
import os
clear = lambda: os.system('clear')

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
    print('Conta valida')
    print(' ')
    
    print('1 - Saldo')
    option_typed = input('Escolha uma das opções acima: ')
    if option_typed == '1':
        print(' ')
        print('Seu saldo é %s' % accounts_list[account_typed]['value'])

else:
    print('Conta inválida')

## agência, senha, nome, valor


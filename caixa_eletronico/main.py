# coding=utf-8

print(' ')
print("*******************************************")
print("*********** Caixa Eletrônico  *************")
print("*******************************************")
print(' ')

import getpass

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')

## print(account_typed)
## print(password_typed)

accounts_list = {
    '0001-02': {
        'agency': '0001-02',
        'password': '01',
        'name': 'João da Silva',
        'value': 0,
    },
    '0002-02': {
        'agency': '0002-02',
        'password': '02',
        'name': 'Maria da Silva',
        'value': 0,
    },
}

if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    print('Conta valida')
else:
    print('Conta inválida')

## agência, senha, nome, valor


# coding=utf-8

print(' ')
print("*******************************************")
print("*********** Caixa Eletrônico  *************")
print("*******************************************")
print(' ')

import getpass

account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')

print(account_typed)
print(password_typed)


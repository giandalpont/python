import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def header():
    print(' ')
    print("*******************************************")
    print("*********** Caixa Eletrônico  *************")
    print("*******************************************")
    print(' ')

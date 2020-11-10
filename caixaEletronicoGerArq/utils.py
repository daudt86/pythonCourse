import os


color = {
    'verde': '\033[1;32m',
    'cyano': '\033[1;36m',
    'azul': '\033[1;34m',
    'vermelho': '\033[1;31m',
    'reset': '\033[0;0m'
}


def header():
    print(color['verde'])
    print('**********************************************************')
    print('******************* CAIXA ELETRONICO *********************')
    print('**********************************************************')
    print(color['reset'])


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

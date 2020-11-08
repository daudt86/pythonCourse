import getpass
import os

color = {
    'verde': '\033[1;32m',
    'cyano': '\033[1;36m',
    'azul': '\033[1;34m',
    'vermelho': '\033[1;31m',
    'reset': '\033[0;0m'
}
accounts_list = {
        '0001-02': {
            'password': '123456',
            'name': 'Fulano da Silva',
            'value': 120,
            'admin': False
        },
        '0002-02': {
            'password': '123456',
            'name': 'Beltrano da Silva',
            'value': 50,
            'admin': False
        },
        '1111-11': {
            'password': '123456',
            'name': 'Admin da Silva',
            'value': 1000,
            'admin': True
        }
    }

money_slips = {
    '20' : 5,
    '50' : 5,
    '100' : 5
}
while True:
    print(color['verde'])
    print('**********************************************************')
    print('******************* CAIXA ELETRONICO *********************')
    print('**********************************************************')
    print(color['reset'])

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass(prompt='Digite sua senha: ')


    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(color['verde'])
        print('**********************************************************')
        print('******************* CAIXA ELETRONICO *********************')
        print('**********************************************************')
        print(color['reset'])

        print('1 - SALDO')
        print('2 - SAQUE')
        if accounts_list[account_typed]['admin']:
            print('10 - INCLUIR CÉDULAS')

        option_typed = input('Escolha uma das opções acima: ')

        if option_typed == '1':
            print('Seu saldo é: %s' % accounts_list[account_typed]['value'])
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input('Valor a ser sacado: ')
            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user[100] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user[50] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user[20] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('O caixa não tem cédulas disponíveis para este saque')
            else:
                for money_bill in money_slips_user:
                    money_slips[str(money_bill)] -= money_slips_user[money_bill]
                print('Pegue as notas:')
                for key, item in money_slips_user.items():
                    print(f'{item} x {key}')
                    accounts_list[account_typed]['value'] += int(item) * key


    else:
        print(f"{color['vermelho']} Conta inválida")
    input('Pressione <ENTER> para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

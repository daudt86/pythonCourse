import getpass
from bank_account_variables import money_slips, accounts_list
from file import save_money_slips


def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and accounts_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '2':
        with_draw(account_auth)


def show_balance(account_auth):
    print('Seu saldo é: %s' % accounts_list[account_auth]['value'])


def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')
    money_slips[money_bill_typed] += int(amount_typed)
    print(money_slips)


def with_draw(account_auth):
    value_typed = input('Valor a ser sacado: ')
    money_slips_user = {}
    value_int = int(value_typed)

    value_int = with_draw_operation(100, value_int, money_slips_user)
    value_int = with_draw_operation(50, value_int, money_slips_user)
    value_int = with_draw_operation(20, value_int, money_slips_user)

    if value_int != 0 or not value_int:
        print('O caixa não tem cédulas disponíveis para este saque')
    else:
        for money_bill in money_slips_user:
            money_slips[str(money_bill)] -= money_slips_user[money_bill]
            save_money_slips()
        print('Pegue as notas:')
        for key, item in money_slips_user.items():
            print(f'{item} x {key}')
            accounts_list[account_auth]['value'] += int(item) * key


def with_draw_operation(money_bill, value_int, money_slips_user):
    if (value_int == None):
        return False

    if value_int // money_bill > 0 and value_int // money_bill <= money_slips[str(money_bill)]:
        money_slips_user[money_bill] = value_int // money_bill
        return value_int - value_int // money_bill * money_bill


def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass(prompt='Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False


def account_menu_options_typed(account_auth):
    print('1 - SALDO')
    print('2 - SAQUE')
    if accounts_list[account_auth]['admin']:
        print('10 - INCLUIR CÉDULAS')

    return input('Escolha uma das opções acima: ')

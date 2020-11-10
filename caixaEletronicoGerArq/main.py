import operations
from bank_account_variables import money_slips, accounts_list
from file import load_bank_data
from utils import clear, header, color


def main():
    header()
    load_bank_data()
    print(accounts_list)
    account_auth = operations.auth_account()

    if account_auth:
        clear()

        header()
        option_typed = operations.account_menu_options_typed(account_auth)
        operations.do_operation(option_typed, account_auth)
    else:
        print(f"{color['vermelho']} Conta inválida")

while True:
    main()
    input('Pressione <ENTER> para continuar...')
    clear()

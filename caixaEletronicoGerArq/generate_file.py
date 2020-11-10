from utils import header
from file import write_money_slips, open_file_bank, write_bank_account


def main():
    header()
    make_money_slips('w')
    file = open_file_bank('a')
    file.write('\n')
    file.close()
    make_bank_account('a')


def make_money_slips(mode):
    file = open_file_bank(mode)
    write_money_slips(file)
    file.close()
    print('Cédulas geradas com sucesso')


def make_bank_account(mode):
    file = open_file_bank(mode)
    write_bank_account(file)
    file.close()
    print('Contas geradas com sucesso')


main()

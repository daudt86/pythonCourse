import os

from bank_account_variables import money_slips, accounts_list

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def open_file_bank(mode):
    return open(BASE_PATH + '/_bank_file.dat', mode)


def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill+'='+str(value)+';')


def write_bank_account(file):
    for account, value in accounts_list.items():
        file.writelines((
            account, ';',
            value['name'], ';',
            value['password'], ';',
            str(value['value']), ';',
            str(value['admin']), ';',
            '\n'
        ))


def read_bank_account(file):
    lines = file.readlines()
    del lines[0]
    for line in lines:
        if line:
            set_bank_account(line)


def set_bank_account(line):
    item_account = line.split(';')
    accounts_list[item_account[0]] = {
        'name': item_account[1],
        'password': item_account[2],
        'value': float(item_account[3]),
        'admin': True if item_account[4] == 'True' else 'False',
    }


def read_money_slips(file):
    line = file.readline()
    lines = line.split(';')
    for item in lines:
        if item and item != '\n':
            set_money_bill_value(item)


def set_money_bill_value(item_line):
    money_item = item_line.split("=")
    money_slips[money_item[0]] = int(money_item[1])


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()

    file = open_file_bank('r')
    read_bank_account(file)
    file.close()


def save_money_slips():
    file = open_file_bank('r')
    lines = file.readlines()
    file.close()
    file = open_file_bank('w')
    lines[0] = ""
    for money_bill, value in money_slips.items():
        lines[0] += money_bill + '=' + str(value) + ';'
    lines[0] += '\n'
    file.writelines(lines)
    file.close()

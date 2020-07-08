import os
from data import money_slips

base_path = os.path.dirname(os.path.abspath(__file__))

file = open(base_path + '/__files_test.dat', 'a') #write
# file.write('\n')
# file.write('Gian Dal Pont\n')
# file.write('100 anos\n')
# file.write('100 anos\n\n')
# file.writelines(('\n - 111111', '\n - 222222', '\n - 33333'))
# file.writelines(['\n - 111111', '\n - 222222', '\n - 33333'])

# file.close()

def open_file_bank(mode):
    return open(base_path + '/_bank_file.dat', mode)

## 20=5; 50=5; 100=5
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')

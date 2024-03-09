from Classes import Bank, Card, Transaction, Owner

options = {
    '0': {
        '1': [1, 'Banks'],
        '2': [2, 'Cards'],
        '3': [3, 'Transactions'],
    },
}
stage = 0

if __name__ == '__main__':
    while True:
        if stage == 0:
            print('Welcome to your personal wallet manager.')
            print('select an option:')
            for key, value in options[str(stage)].items():
                print(f'{key}) {value[1]}')
            print(f'0) go back')
            print(f'q) exit')
        elif stage == 1:
            print('List of your Banks:')
        elif stage == 2:
            print('List of your Cards:')
        elif stage == 3:
            print('List of your Transactions:')
        else:
            stage = 0

        stage = input()
        if stage == 'q':
            break
        elif stage.isnumeric(): # go back if input==0
            stage = int(stage)
        else:
            stage = 0

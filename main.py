import json
import os

from Classes import Bank, Card, Transaction, Owner

with open('bin/stages.json', 'r') as f:
    stages = json.load(f)
stage = 0

if __name__ == '__main__':
    while True:
        os.system('cls||clear')
        for msg in stages[str(stage)]['messages']:
            print(msg)
        print('select an option:')
        for key, value in stages[str(stage)]['options'].items():
                print(f'{key}) {value[1]}')

        new_stage = input()
        if new_stage == 'q':
            break
        elif new_stage.isnumeric():
            stage = stages[stage][0]
        else:
            stage = 0

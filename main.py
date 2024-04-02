import json
import os

from Classes import Bank, Card, Transaction, Owner
from DataBase import read_from_db

with open('bin/stages.json', 'r') as f:
    stages = json.load(f)
stage = '0'

if __name__ == '__main__':
    while True:
        os.system('cls||clear')
        
        # print stage messages
        for msg in stages[stage]['messages']:
            print(msg)

        # print stage options
        if stages[stage]['type'] == 'options':
            print('\nselect an option:')
            for key, value in stages[stage]['options'].items():
                    print(f'{key}) {value[1]}')
        
        # print stage list
        elif stages[stage]['type'] == 'list':
            stage_class = stages[stage]['class']
            class_data = read_from_db(stage_class)
            print(class_data)
            
            print('\nselect an option:')
            for key, value in stages[stage]['options'].items():
                    print(f'{key}) {value[1]}')

        print('\nq for quit')

        new_stage = input()
        if new_stage == 'q':  # exit condition
            break
        elif new_stage.isnumeric():  # stage handler
            if new_stage not in stages[stage]['options'].keys():  # handle exceptional numeric entries 
                 stage = '0'
                 continue
            print(stages[stage]['options'][new_stage][0])
            stage = stages[stage]['options'][new_stage][0]
        else:  # handle other exceptional entries
            stage = '0'

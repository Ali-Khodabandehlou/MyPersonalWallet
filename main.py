import importlib
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

        # options stages
        if stages[stage]['type'] == 'options':
            pass
            # print('\nselect an option:')
            # for key, value in stages[stage]['options'].items():
            #     print(f'{key}) {value[1]}')
        
        # list stages
        elif stages[stage]['type'] == 'list':
            stage_class = stages[stage]['class']
            class_data = read_from_db(stage_class)
            print(class_data)

        # functional stages
        elif stages[stage]['type'] == 'func':
            stage_class = stages[stage]['class']
            stage_func = stages[stage]['func']

            _module = __import__('Classes', fromlist=[stage_class])
            _class = getattr(_module, stage_class)
            new_class = _class()
            func = getattr(new_class, stage_func)

            os.system('cls||clear')
            print(func())
            input('press any key to continue')
            stage = stages[stage]['options']['0'][0]
            continue
            
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
            stage = stages[stage]['options'][new_stage][0]
        else:  # handle other exceptional entries
            stage = '0'

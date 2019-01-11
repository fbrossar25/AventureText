import json
import sys

from typing import Dict, List, Sequence
from typing import Union
from typing import Callable
from typing import Any


class TextAdventure:
    def __init__(self, filename: str, start: str):
        self.filename = filename
        self.ppt = self.load_properties()
        self.user_input = {}

    def load_properties(self) -> Any:
        try:
            with open(self.filename, 'r') as f:
                ppt = json.load(f)
            return ppt
        except IOError as e:
            print('IOERROR - {}'.format(str(e)))
            exit(1)

    def print_choice(self, name: str):
        print(self.ppt['description'][name]['text'])
        choices = self.ppt['choix'][name]

        if len(choices) == 1 and ('input' in choices[0]):
            result = input(' > ')
            print(result)
        n = 1
        for choice in choices:
            print('   {n} - {text}'.format(
                n=n,
                text=choice['text']
            ))
            n += 1

    def get_choice(self):
        pass




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No text file for text adventure :'(")
        print("Please enter a file.")
        exit(1)

    filename = sys.argv[1]
    start = 'Intro'

    t = TextAdventure(filename, start)
    t.load_properties()

    print()
    t.print_choice(start)


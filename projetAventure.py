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
        self.global_var = {}
        self.start = start

    def load_properties(self) -> Any:
        # json.decoder.JSONDecodeError
        try:
            with open(self.filename, 'r') as f:
                ppt = json.load(f)
            return ppt
        except IOError as e:
            print('IOERROR - {}'.format(str(e)))
            exit(1)

    def get_global_var(self) -> None:
        for key, value in self.ppt['variables'].items():
            self.global_var[key] = value

    def print_choice(self, name: str) -> bool:
        choices = self.ppt['choix'][name]

        if len(choices) == 1 and ('input' in choices[0]):
            print(self.ppt['description'][name]['text'].format(**self.user_input))
            print()
            print(self.ppt['choix'][name][0]['text'].format(**self.user_input))

            self.user_input[self.ppt['choix'][name][0]['input']] = input(' > ')
            return False

        n = 1
        print(self.ppt['description'][name]['text'])
        for choice in choices:
            print('   {n} - {text}'.format(
                n=n,
                text=choice['text'].format(**self.user_input)
            ))
            n += 1
        return True

    def handle_define(self, choice: str, n: int):
        if "define" in self.ppt['choix'][choice][n]:
            for key, value in self.ppt['choix'][choice][n]["define"].items():
                self.global_var[key] = value

    def get_choice(self, name: str) -> str:
        choice = None 
        if self.print_choice(name):
            while True:
                print('Quel est votre choix ?')
                try:
                    choice = int(input(' > '))
                    if choice <= 0 or choice > len(self.ppt['choix'][name]):
                        continue
                    else:
                        break
                except ValueError:
                    pass

        else:
            choice = 1

        self.handle_define(name, choice-1)
        return self.next_choice(name, choice-1)


    def next_choice(self, name: str, n: int) -> str:
        choice = self.ppt['choix'][name][n]
        if 'require' in choice:
            if self.global_var[choice["require"]["name"]]:
                return choice["require"]["true"]
            else:
                return choice["require"]["false"]

        else:
            return choice['next']


    def loop(self):
        choice = self.start
        while True:
            print()
            print()
            choice = self.get_choice(choice)

            if choice == 'victoire':
                self.trigger_win()
                break

    def trigger_win(self):
        print()
        print(self.ppt['description']['victoire']['text'].format(**self.user_input))




if __name__ == '__main__':
    try:
        filename = 'text.json'
        start = 'Intro'

        t = TextAdventure(filename, start)
        t.load_properties()
        t.get_global_var()
        print()
        t.loop()
    except KeyboardInterrupt:
        print('\r\r\nBye ! :)')
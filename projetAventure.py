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

    def load_properties(self) -> Any:
        try:
            with open(self.filename, 'r') as f:
                ppt = json.load(f)
            return ppt
        except IOError as e:
            print('IOERROR - {}'.format(str(e)))
            exit(1)

    




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No text file for text adventure :'(")
        print("Please enter a file.")
        exit(1)

    filename = sys.argv[1]
    #start = 'Intro'
    start = "foo"

    t = TextAdventure(filename, start)
    t.load_properties(  
    print(json.dumps(t.ppt, indent=2))
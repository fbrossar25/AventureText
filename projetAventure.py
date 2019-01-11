import json
import sys

from typing import Dict, List, Sequence
from typing import Union
from typing import Callable
from typing import Any

def load_properties(filepath : str) -> Any:
    try:
        with open(filepath, 'r') as f:
            ppt = json.load(f)
        return ppt
    except IOError as e:
        print('IOERROR - {}'.format(str(e)))
        exit(1)



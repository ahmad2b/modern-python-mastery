from typing import Dict, Union, Optional
import pprint

Key = Union[int, str]  # create custom type
Value = Union[int, str, list, dict, tuple, set]


data: Dict[Key, Value] = {
    "fname": "Shoukat Ali",
    "name": "Muhammad Ahmad",
    "education": "BSCS",
}

pprint.pprint(data)

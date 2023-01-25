import json
from pathlib import Path
from typing import List, Any

from fastapi.encoders import jsonable_encoder


def search_in_dict_value(values_dict: dict, value: str):

    for item in values_dict:
        if values_dict[item] == value:
            return True
    return False

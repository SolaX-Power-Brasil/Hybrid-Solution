import pytest
import json
from collections import Counter
from test_common import *

def no_duplicated_id(file_path: str) -> bool:
    data = get_data(file_path)
    if data == None: return False

    for key, value in data.items():    
        ids = [item['id'] for item in data[key]]

    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        print(f"Fail - Duplicated ID: {duplicates} - File: {file_path}")
        return False
    else:
        return True


def test_no_duplicated_id():
    for file in files:
        assert no_duplicated_id(file) == True

if __name__ == "__main__":
    test_no_duplicated_id()
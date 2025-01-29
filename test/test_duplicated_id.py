import pytest
import os
import json
from collections import Counter

def no_duplicated_id(file_path: str) -> bool:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for key, value in data.items():    
        ids = [item['id'] for item in data[key]]

    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        print(f"Fail - Duplicated ID: {duplicates} - File: {file_path}")
        return False
    else:
        return True
    

def test_duplicated_id():
    assert no_duplicated_id("../singlePhaseHVBat.json") == True
    assert no_duplicated_id("../splitPhaseHVBat.json") == True
    assert no_duplicated_id("../threePhaseHVBat.json") == True



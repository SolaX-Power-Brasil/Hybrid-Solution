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
    

folder = "../"
files = ["singlePhaseHVBat.json", "threePhaseHVBat.json", "splitPhaseHVBat.json"]
for idx, file in enumerate(files):
    if no_duplicated_id(folder + file): print(f"Pass - Duplicated ID: {file} ")

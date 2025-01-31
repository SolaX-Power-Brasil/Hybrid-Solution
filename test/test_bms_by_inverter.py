import pytest
import json
from collections import Counter
from test_common import files

"""
Test if nominal power (Pn) times number of inverters is correct 
"""

def bms_by_inverter(file_path: str) -> bool:

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            inverter_count = solution['inverter']['quantity']
            bms_count = 0
            for accessory in solution['accessories']:
                if accessory['model'] == "BMS-Parallel Box-II G2":
                    bms_count = accessory['quantity'] 
                
            if bms_count > 0:
                if inverter_count == bms_count: 
                    print(f"{solution['id']}: ok")
                else: 
                    print(f"Fail - Inverter->BMS match: {solution['id']} - File: {file_path}")
                    return False
    return True

    
def test_bms_by_inverter():
    for file in files:
        assert bms_by_inverter(file) == True

if __name__ == "__main__":
    test_bms_by_inverter()


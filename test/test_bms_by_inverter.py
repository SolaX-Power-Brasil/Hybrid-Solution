import pytest
import json
from collections import Counter
from test_common import *

"""
Test if nominal power (Pn) times number of inverters is correct 
"""

def bms_by_inverter(file_path: str) -> bool:

    data = get_data(file_path)
    if data == None: return False


    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            inverter_count = get_inverter_number(solution)
            bms_count = 0
            for accessory in solution['accessories']:
                if accessory['model'] == accs.bms:
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


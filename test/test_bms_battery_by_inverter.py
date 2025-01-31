import pytest
import json
from collections import Counter
from test_common import files

"""
Test if nominal number of batteries, BMS and inverters are correct 
"""

def bms_battery_by_inverter(file_path: str) -> bool:

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
     
    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            inverters = solution['inverter']['quantity']
            batteries = solution['battery']['quantity']
            bms_count = 0
            for accessory in solution['accessories']:
                if accessory['model'] == "BMS-Parallel Box-II G2":
                    bms_count = accessory['quantity'] 

            if bms_count > 0:
                battery_by_inverter = batteries / inverters
                bms_battery_ports = 2
                if battery_by_inverter % bms_battery_ports == 0: 
                    print(f"{solution['id']}: ok")
                else: 
                    print(f"Fail - Inverter->BMS->Battery match: {solution['id']} - File: {file_path}")
                    return False
    return True

    
def test_bms_battery_by_inverter():
    for file in files:
        assert bms_battery_by_inverter(file) == True

if __name__ == "__main__":
    test_bms_battery_by_inverter()


import pytest
import json
from collections import Counter
from test_common import *

"""
Test if nominal number of batteries, BMS and inverters are correct 
"""
def bms_battery_by_inverter(file_path: str) -> bool:

    data = get_data(file_path)
    if data == None: return False

    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            bms_count = [(bms_['quantity']) for bms_ in solution['accessories'] if bms_['model'] == accs.bms ]
            if bms_count != []:                
                battery_by_inverter = get_battery_quantity(solution) / get_inverter_number(solution)
                bms_battery_ports = 2
                if battery_by_inverter % bms_battery_ports != 0: 
                    print(f"Fail - Battery->BMS->Inverter: {solution['id']} - File: {file_path}")
                    return False
                
                print(f"{solution['id']}: ok")
                return True
    
    return True

def test_bms_battery_by_inverter():
    for file in files:
        assert bms_battery_by_inverter(file) == True

if __name__ == "__main__":
    test_bms_battery_by_inverter()


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
     
    root_values   = [ value for key, value in data.items() ]
    solutions_set = [ solution for solution in root_values[0: len(root_values)] ]
    solutions     = [ solution_set for solution_set in solutions_set[0: len(solutions_set)] ]

    for idx, solution in enumerate(solutions):
        inverters = solution[idx]['inverter']['quantity']
        batteries = solution[idx]['battery']['quantity']
        bms = [ accs for accs in solution[idx]['accessories'] if accs['model'] == "BMS-Parallel Box-II G2" ]
        if bms: 
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


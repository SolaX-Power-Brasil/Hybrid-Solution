import pytest
import json
from collections import Counter
from test_common import inverters_peak_power, files

"""
Test if [ (Pn) * Number of inverters ] is correct 
"""

def inverter_peak_power_match(file_path: str) -> bool:

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for key, value in data.items():
        #print(f"{value}")   
        for idx,solution in enumerate(data[key]):
            inverter = solution['inverter']
            quantity: int =inverter['quantity']
            solution_power: int =inverter['peakPowerW']
            inverter_power = inverters_peak_power.get(inverter['model'], 0)
            if inverter_power * quantity == solution_power: 
                print(f"Peak Power - OK: {solution['id']}")
            else: 
                print(f"Fail - Wrong Peak Power: {solution['id']} - File: {file_path}")
                return False

    return True

    
def test_inverter_power():
    for file in files:
        assert inverter_peak_power_match(file) == True

if __name__ == "__main__":
    test_inverter_power()


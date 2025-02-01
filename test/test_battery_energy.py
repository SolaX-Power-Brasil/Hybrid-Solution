import pytest, json
from collections import Counter
from test_common import *

"""
Test if nominal power (Pn) times number of inverters is correct 
"""

def inverter_power_match(file_path: str) -> bool:

    data = get_data(file_path)
    if data == None: return False

    for key, value in data.items():
        #print(f"{value}")   
        for idx,solution in enumerate(data[key]):
            battery = solution['battery']
            battery_count: int =battery['quantity']
            solution_battery_energy: int =battery['availableEnergyWh']
            single_battery_energy = batteries_useful_energy.get(battery['model'], 0)
                
            if single_battery_energy * battery_count == solution_battery_energy: 
                print(f"{solution['id']}: ok")
            else: 
                print(f"Fail - Battery energy: {solution['id']} - File: {file_path}")
                return False

    return True

    
def test_inverter_power():
    for file in files:
        assert inverter_power_match(file) == True

if __name__ == "__main__":
    test_inverter_power()


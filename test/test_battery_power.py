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
            battery_count: int = get_battery_quantity(solution)
            single_battery_power = batteries_standard_power.get(get_battery_model(solution), 0)
            
            bms_count = [(bms_['quantity']) for bms_ in solution['accessories'] if bms_['model'] == accs.bms ]
            if bms_count != []:
                battery_count /= 2 # Using BMS reduce the power to the half
                
            if single_battery_power * battery_count == get_battery_powerW(solution): 
                print(f"{solution['id']}: ok")
            else: 
                print(f"Fail - Battery power: {solution['id']} - File: {file_path}")
                return False

    return True


def test_inverter_power():
    for file in files:
        assert inverter_power_match(file) == True

if __name__ == "__main__":
    test_inverter_power()


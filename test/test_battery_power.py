import pytest, json
from collections import Counter
from test_common import files, batteries_standard_power, accessories

"""
Test if nominal power (Pn) times number of inverters is correct 
"""

def inverter_power_match(file_path: str) -> bool:

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for key, value in data.items():
        #print(f"{value}")   
        for idx,solution in enumerate(data[key]):
            battery = solution['battery']
            battery_count: int =battery['quantity']
            solution_battery_power: int =battery['powerW']
            single_battery_power = batteries_standard_power.get(battery['model'], 0)
            
            for accessory in solution['accessories']:
                if accessory['model'] == accessories['bms']:
                    battery_count /= 2 # Using BMS reduce the power to the half
                
            if single_battery_power * battery_count == solution_battery_power: 
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


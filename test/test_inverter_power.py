import pytest
import os
import json
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
            inverter = solution['inverter']
            quantity: int =inverter['quantity']
            solution_power: int =inverter['ratedPowerW']
            inverter_power = inverters_rated_power.get(inverter['model'], 0)
            if inverter_power * quantity == solution_power: 
                print(f"{solution['id']}: ok")
            else: 
                print(f"Fail - Wrong Power: {solution['id']} - File: {file_path}")
                return False

    return True

    
def test_inverter_power():
    for file in files:
        assert inverter_power_match(file) == True

if __name__ == "__main__":
    test_inverter_power()


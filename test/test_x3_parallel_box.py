import pytest, json
from collections import Counter
from test_common import *

"""
Test if Parallel Box is correct 
"""

def inverter_power_match(file_path: str) -> bool:

    data = get_data(file_path)
    if data == None: return False

    for key, value in data.items():   
        for idx,solution in enumerate(data[key]):
            x3_pbox_60KW_count = get_x3_pbox_60_number(solution)
            x3_pbox_150KW_count = get_x3_pbox_150_number(solution)
            inverters_count = get_inverter_number(solution)
            inverters_power = get_inverter_powerW(solution)            
            x3_pbox_60KW_powerW = 60000
            x3_pbox_150KW_powerW = 150000
            limit_without_x3_pbox = 3
            
            if(inverters_count <= limit_without_x3_pbox):
                print(f"{solution['id']}: ok")
                continue

            if (x3_pbox_60KW_count != []) and (inverters_power <= x3_pbox_60KW_powerW):
                print(f"{solution['id']}: ok")
                continue
                
            if (x3_pbox_150KW_count != [] ) and (inverters_power <= x3_pbox_150KW_powerW):
                print(f"{solution['id']}: ok")
                continue
 
            print(f"Fail - X3-EPS Parallel Box: {solution['id']} - File: {file_path}")
            return False

    return True


def test_inverter_power():
    for file in files:
        assert inverter_power_match(file) == True

if __name__ == "__main__":
    test_inverter_power()


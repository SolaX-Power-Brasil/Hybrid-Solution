import requests
import time
from test_common import *


api_ep_patch = 'https://x8ki-letl-twmt.n7.xano.io/api:aM7RxPFv/sugestoes_teste'
header= { 'Content-Type': 'application/json' }
json_suggestion = { 
    "sugestoes_teste_id": 1,
    "name":  "parallelInverter_7.5K_T58-104",
    "inverter_model":  "X1-HYBRID-7.5-D",
    "inverter_quantity": 2,
    "inverter_nominalVoltageV": 150,
    "inverter_ratedPowerW": 200,
    "inverter_peakPowerW": 200,
    "battery_model":  "T58",
    "battery_quantity": 0,
    "battery_powerW": 0,
    "battery_availableEnergyWH": 0,
    "acessories": [],
    "matebox":  "false",
    "comments":  { 
        "text" :  "null"
    },
    "type":  "singlePhase220V",
    "inverter_image":  "null",
    "battery_image":  "null"  
}


def update_single_record(solution: str = None) -> bool:
    if solution == None: return False

    json_suggestion["name"] = get_solution_id(solution=solution)
    json_suggestion["inverter_model"] = get_inverter_model(solution=solution)
    json_suggestion["inverter_quantity"] = get_inverter_number(solution=solution)
    json_suggestion["inverter_nominalVoltageV"] = get_inverter_voltage(solution=solution)
    json_suggestion["inverter_ratedPowerW"] = get_inverter_powerW(solution=solution)
    json_suggestion["inverter_peakPowerW"] = get_inverter_peak_powerW(solution=solution)
    json_suggestion["battery_model"] = get_battery_model(solution=solution)
    json_suggestion["battery_quantity"] = get_battery_quantity(solution=solution)
    json_suggestion["battery_powerW"] = get_battery_powerW(solution=solution)
    json_suggestion["battery_availableEnergyWH"] = get_battery_energyWh(solution=solution)

    time.sleep(2) # Máx. 10 requisições por segundo 
    response = requests.patch(url=api_ep_patch, headers=header, json=json_suggestion)
    print(response)
    return response.ok


if __name__ == "__main__":
    data = get_data("/home/marcelo/dev/solax/tool/Hybrid-Solution/singlePhase_220_HVBat.json")
    if data == None:
        ...
    else:
        for key, value in data.items():   
            for idx,solution in enumerate(data[key]):
                if update_single_record(solution=solution) == False:
                    break
    print("Finished")
                

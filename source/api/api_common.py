
import os
import requests
import time
from dotenv import load_dotenv
from test_common import *


load_dotenv()

header= { 'Content-Type': 'application/json' }
json_template: dict = { 
    "sugestoes_id": 1,
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
    "comments":  "",
    "type":  "1p_220_hv_bat",
    "inverter_image":  "https://x8ki-letl-twmt.n7.xano.io/vault/20xZAPgJ/9xtkzd1N6brKDP1-TsQDkJW_os0/iAPJSA../X3.png",
    "battery_image":  "https://x8ki-letl-twmt.n7.xano.io/vault/20xZAPgJ/oZBREvTGKimE2Q-etwM7OTucc4E/Bdtuzg../T58.png"  
}


class db_inverter_type:
    singlePhase_220_hv_bat: str = 'singlePhase220V' #'1p_220_hv_bat'
    singlePhase_220_lv_bat: str = '1p_220_lv_bat'
    splitPhase_220_hv_bat:  str = '2p_220_hv_bat'
    threePhase_220_hv_bat:  str = '3p_220_hv_bat'
    threePhase_380_hv_bat:  str = '3p_380_hv_bat'


def get_inverter_type(solution: str = None) -> db_inverter_type:
    model = get_inverter_model(solution=solution)
    
    if model == "X1-HYBRID-5.0-D" or \
       model == "X1-HYBRID-7.5-D":
        return db_inverter_type.singlePhase_220_hv_bat
    elif model == "X1-SPT-6K":
        return db_inverter_type.splitPhase_220_hv_bat
    elif model == "X3-HYBRID-8.3-D LV":
        return db_inverter_type.threePhase_220_hv_bat
    elif model == "X3-HYBRID-15.0-D":
        return db_inverter_type.threePhase_380_hv_bat
    else:
        raise TypeError(f"Inversor modelo: {model} inválido")
    

def populate_template(template:dict = None, solution:str = None) -> bool:
    if None == template or None == solution: 
        return False
    #Solution
    template["name"] = get_solution_id(solution=solution)
    #Inverters
    template["type"]                     = get_inverter_type(solution=solution)
    template["inverter_model"]           = get_inverter_model(solution=solution)
    template["inverter_quantity"]        = get_inverter_number(solution=solution)
    template["inverter_nominalVoltageV"] = get_inverter_voltage(solution=solution)
    template["inverter_ratedPowerW"]     = get_inverter_powerW(solution=solution)
    template["inverter_peakPowerW"]      = get_inverter_peak_powerW(solution=solution)
    #Batteries
    template["battery_model"]             = get_battery_model(solution=solution)
    template["battery_quantity"]          = get_battery_number(solution=solution)
    template["battery_powerW"]            = get_battery_powerW(solution=solution)
    template["battery_availableEnergyWH"] = get_battery_energyWh(solution=solution)
    #Accessories    
    template["acessories"] = get_accessories(solution=solution)
    template["matebox"]    = get_external_ats(solution=solution)
    #Comments
    template['comments'] = ""
    comments: list = get_comments(solution=solution)
    if comments != None:
        for comment in comments:
            if comment != None:
                template['comments'] += comment.replace("[", "").replace("]", "").replace("'", "")
    return True

def insert_single_record(solution: str = None, url_api: str = None) -> bool:
    if solution == None or url_api == None: 
        return False
    if not populate_template(template=json_template, solution=solution):
        return False

    time.sleep(2) #Evita o excesso de requisições  
    response = requests.post(url=url_api, headers=header, json=json_template)    
    print(response)
    return response.ok


def insert_all_records(data: dict = None, url_api: str = None) -> bool:
    if data == None: return False
    for key, value in data.items():   
        for idx,solution in enumerate(data[key]):
            insert_single_record(solution=solution, url_api=url_api)
    return True

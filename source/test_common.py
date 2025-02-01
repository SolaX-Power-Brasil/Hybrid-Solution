"""
Common attributes for all tests
"""

import json

#Carrega JSON
def get_data(file_path: str) -> any:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    return None

#Imprime uma solução
def print_solution(solution=None) -> None:
    line = "----------------------------------------------------------"        
    print(f"{bcolors.OKGREEN}{line}\n Sugestão recomendada \n{line}{bcolors.ENDC}")
    print(solution)
    return

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


inverters_rated_power = {
    "X1-HYBRID-5.0-D":    5000, 
    "X1-HYBRID-7.5-D":    7500,
    "X1-SPT-6K":          6000,
    "X3-HYBRID-5.5-D LV": 5500,
    "X3-HYBRID-8.3-D LV": 8300,
    "X3-HYBRID-15.0-D":   15000
}

inverters_peak_power = {
    "X1-HYBRID-5.0-D":    7500,
    "X1-HYBRID-7.5-D":    11250,
    "X1-SPT-6K":          7200,
    "X3-HYBRID-5.5-D LV": 8250,
    "X3-HYBRID-8.3-D LV": 12450,
    "X3-HYBRID-15.0-D":   22500
}

batteries_standard_power = {
    "T58": 2875
}
batteries_useful_energy = {
    "T58": 5175
}

class accs:
    x1_matebox   = "X1-Matebox Advanced"
    x3_matebox   = "X3-Matebox Advanced"
    x3_pbox_60k  = "X3-PBOX-60kW-G2"
    x3_pbox_150k = "X3-PBOX-150kW-G2"
    bms          = "BMS-Parallel Box-II G2"
    meter        = "Smart Meter"

accessories = {
    'x1_matebox'  : "X1-Matebox Advanced",
    'x3_matebox'  : "X3-Matebox Advanced",
    'x3_pbox_60k' : "X3-PBOX-60kW-G2",
    'x3_pbox_150k': "X3-PBOX-150kW-G2", 
    'bms'         : "BMS-Parallel Box-II G2",
    'meter'       : "Smart Meter"
}

comment_rated_peak_power = "Para operar na potência nominal e de pico (10 segundos) será necessário ter potência FV ( Potência Inversor - Potência Bateria )."
comment_peak_poer = "Para operar na potência de pico (10 segundos) será necessário ter potência FV ( Potência Inversor - Potência Bateria )."
comment_x3_epsbox = "Verifique os limites operacionais da X3-EPS Parallel Box G2 na documentação técnica (Datasheet e Manuais)."
comment_smart_meter = "O Smart Meter deve ser compatível com os inversores SolaX, verifique a disponibilidade com seu distribuidor."

singlePhase_files = {
    "../singlePhase_220_HVBat.json"
}
splitPhase_files = {
    "../splitPhase_220_HVBat.json"
}
threePhase_220V_files = {
    "../threePhase_220_HVBat.json"
}
threePhase_380V_files = {
     "../threePhase_380_HVBat.json"
}

files = {
    "../singlePhase_220_HVBat.json",
    "../splitPhase_220_HVBat.json",
    "../threePhase_380_HVBat.json",
    "../threePhase_220_HVBat.json"
    ## ,"../threePhase_220_5_5K_HVBat.json"
}

def inverter_peak_powerW(solution) -> int: return int( solution['inverter']['peakPowerW'] )
def get_inverter_number(solution)  -> int: return int( solution['inverter']['quantity'] )
def inverter_model(solution)       -> str: return str( solution['inverter']['model'] )

def battery_powerW(solution)       -> int: return int( solution['battery']['powerW'] )
def battery_energyWh(solution)     -> int: return int( solution['battery']['availableEnergyWh'] )
def battery_quantity(solution)     -> int: return int( solution['battery']['quantity'] )
def battery_model(solution)        -> str: return str( solution['battery']['model'] )


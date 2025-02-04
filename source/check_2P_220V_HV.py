"""
TESTA APLICAÇÔES MONOFÁSICAS 
"""

import sys
from test_common import *
from check_common import *


def splitPhase_solution(file_path: str, \
                        load_powerW=0, load_peak_powerW=0, load_energyWh=0 , pv_available=0) -> bool:
    data = get_data(file_path)
    if data == None: return False

    #Dados para teste
    if not load_powerW: load_powerW = int(input("Potência de regime da carga [W]:"))
    if not load_peak_powerW: load_peak_powerW = int(input("Potência de pico da carga [W]: "))
    if not load_energyWh: load_energyWh = int(input("Energia necessária [Wh]:"))
    
    values_make_sense = load_powerW <= load_peak_powerW
    if not values_make_sense: 
        logger.info(f"Confira os valores: Pn:{load_powerW} <= Ppico: {load_peak_powerW}")
        return False

    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            if test_solution(pv_available, load_powerW, load_peak_powerW, load_energyWh, solution):
                return True   
    return False
    
if __name__ == "__main__":
    if len(sys.argv) == 4:
        ld_pwr = int(sys.argv[1])
        ld_peak_pwr = int(sys.argv[2])
        ld_energy = int(sys.argv[3])
        if splitPhase_solution(next(iter(splitPhase_files)), ld_pwr, ld_peak_pwr, ld_energy) == False:
            logger.info(f"Solução não encontrada. Confira se os dados estão corretos.")
    else:
        print("Erro: São necessários 3 valores: LoadPowerW LoadPeakPowerW LoadEnergyWh")


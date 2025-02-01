"""
TESTA APLICAÇÔES MONOFÁSICAS 
"""

from test_common import *


def test_solution(pv_available, load_peak_powerW, load_energyWh, solution) -> bool:    
    energy_match: bool = \
        load_energyWh <= battery_energyWh(solution)        ##SEM FV - A energia vem sempre das baterias
    power_battery_match: bool = \
        load_peak_powerW <= battery_powerW(solution) and \
        load_peak_powerW <= inverter_peak_powerW(solution) ##SEM FV. Toda a potência é retirada da bateria          
    power_battery_pv_match: bool = \
        load_peak_powerW <= inverter_peak_powerW(solution) ##COM FV. FV tem potência para operar o inversor na potência de pico          
    
    if energy_match:
        if pv_available:
            if power_battery_pv_match:
                print_solution(solution)
                return True
            else:
                print(f"Falha -  Pot. Pico do Inversor #{solution['id']}")
        else: 
            if power_battery_match:
                print_solution(solution)
                return True
            else:
                print(f"Falha - Potência da(s) Bateria(s) #{bcolors.FAIL + solution['id'] + bcolors.ENDC} ")
    else:
        print(f"Falha - Energia da(s) bateria(s) #{bcolors.FAIL + solution['id'] + bcolors.ENDC}")
    
    return False


def singlePhaseSolution(file_path: str, \
                        load_powerW=0, load_peak_powerW=0, load_energyWh=0) -> bool:
    data = get_data(file_path)
    if data == None: return False

    #Dados para teste
    load_powerW = int(input("Digite a potência de regime da carga [W]:"))
    load_peak_powerW = int(input("Digite a potência de pico da carga [W]: "))
    load_energyWh = int(input("Digite a energia necessária [Wh]:"))
    pv_available = int(input("Considerar o FV? [1=Sim/0=Não)]:"))
    
    values_make_sense = load_powerW <= load_peak_powerW
    if not values_make_sense: return False

    for key, value in data.items():
        for idx,solution in enumerate(data[key]):
            if test_solution(pv_available, load_peak_powerW, load_energyWh, solution):
                return True   
    return False

    
if __name__ == "__main__":
    if singlePhaseSolution(next(iter(singlePhase_files))) == False:
        print("Solução não encontrada. Confira se os dados estão corretos")


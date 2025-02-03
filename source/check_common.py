"""
TESTA APLICAÇÔES MONOFÁSICAS 
Copyright meu ovo (c), 2025
"""
import logging
from test_common import *

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=f'logger.log', 
                    filemode="a+",
                    level=logging.INFO)


def test_solution(pv_available, load_power, load_peak_powerW, load_energyWh, solution) -> bool:    
    energy_match: bool = \
        load_energyWh <= get_battery_energyWh(solution)        ##SEM FV - A energia vem sempre das baterias
    
    power_with_pv_match: bool = \
              load_power <= get_inverter_powerW(solution) and \
        load_peak_powerW <= get_inverter_peak_powerW(solution) ##COM FV. Toda a potência é retirada do fotovoltaico          
    
    power_without_pv_match: bool = \
        power_with_pv_match and \
        load_peak_powerW <= get_battery_powerW(solution)      ##SEM FV. Toda a potência é retirada da bateria
    
    if not energy_match: 
        return False
    
    if ((not pv_available) and power_without_pv_match) or \
            (pv_available and power_with_pv_match):    
        logger.info(f'"PV available:": {pv_available==1}, "Pn[W]": {load_power}; "Ppico[W]": {load_peak_powerW}; "Energy[Wh]": {load_energyWh}')
        logger.info(solution)      
        return True
        
    return False


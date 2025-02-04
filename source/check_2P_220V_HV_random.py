"""
TESTA APLICAÇÔES BIFÁSICAS 
"""

import sys
import random
from check_2P_220V_HV import *


#Verifica as soluções criando números aleatórios
# argv[1] = Numero de iterações
if __name__ == "__main__":
    if len(sys.argv) == 2:
        num_tests = int(sys.argv[1])

        ld_power_limitW = 12000
        ld_peak_power_limitW = 14400
        ld_energy_limitWh = 31050

        while num_tests > 0:
            num_tests-= 1
            step = 750
            init_value = 1
            ld_power = random.randrange(init_value, ld_power_limitW, step)
            ld_peak_power = random.randrange(ld_power, ld_peak_power_limitW, step)
            ld_energy = random.randrange(init_value, ld_energy_limitWh, step)
            if splitPhase_solution(next(iter(splitPhase_files)), ld_power, ld_peak_power, ld_energy) == False:
                logger.info(f"Solução não encontrada. Confira se os dados estão corretos.")



"""
TESTA APLICAÇÔES BIFÁSICAS 
"""

import sys
import random
from check_3P_220V_HV import *


#Verifica as soluções criando números aleatórios
# argv[1] = Numero de iterações
if __name__ == "__main__":
    if len(sys.argv) == 2:
        num_tests = int(sys.argv[1])

        ld_power_limitW = 83000
        ld_peak_power_limitW = 115000
        ld_energy_limitWh = 414000

        while num_tests > 0:
            num_tests-= 1
            init_value = 1
            delta = random.randrange(start=1, stop=1000, step=1)
            ld_power = random.randrange(start=init_value, stop=ld_power_limitW, step=delta)
            ld_peak_power = random.randrange(start=ld_power, stop=ld_peak_power_limitW, step=delta)
            ld_energy = random.randrange(start=init_value, stop=ld_energy_limitWh, step=delta)
            if threePhase_220V_solution(next(iter(threePhase_220V_files)), ld_power, ld_peak_power, ld_energy) == False:
                logger.info(f"Solução não encontrada. Confira se os dados estão corretos.")



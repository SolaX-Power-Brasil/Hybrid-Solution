# Soluções SolaX Power - Sistemas Residenciais
Informações em formato JSON sobre as possíveis combinações de produtos híbridos da SolaX Power para soluções de armazenamento.  

## Formato da estrutura dos dados
```
 "setOfSolutionsForEspecificTechnology": 
 [
    {
       "id": "singleInverter_T58-002",  
       "inverter": { "model": "X3-HYBRID-15.0-D", "quantity": 1, "nominalVoltageV": 380, "ratedPowerKW": 15.0, "peakPowerKW": 22.5 },  
       "battery": { "model": "T58", "quantity": 2, "powerKW": 5.7, "availableEnergyKWH": 10.4 },  
       "accessories":
       [
          { "model": null, "quantity": 0 }
       ],  
       "comments":
       [
          "Para operar na potência nominal e de pico (10 segundos) será necessário ter potência FV ( Potência Inversor - Potência Bateria )."
       ]
    },
    {
        Próxima solução...
    }
]
```
### Explicação detalhada
- id: Identificação unívoca de cada solução (Inversores_Bateria - Sequência Numérica)
- inverter
  - **model**: Modelo oficial do inversor (conforme consta no datasheet)
  - **quantity**: Quantos inversores estão presentes em cada solução
  - **nominalVoltageV**: Tensão nominal de operação (Para sistemas monofásicos é a tensão Fase-Neutro, para sistemas trfásicos é a tensão Fase-Fase)
  - **ratedPowerW**: Potência de regime (nominal) combinada de todos os inversores da solução.
  - **peakPowerW**: Potência de pico (normalmente 10 segundos ou 20 segundos) combinada de todos os inversores da solução.
 
- battery
  - **model**: Modelo oficial da bateria (conforme consta no datasheet)
  - **quantity**: Quantas baterias estão presentes em cada solução
  - **powerW**: Potência padrão combinada de todas as baterias da solução
  - **availableEnergyWh**: Energia disponível (descontando os 10% da energia total) de todas as baterias da solução
  
- accessories
  - **model**: Modelo oficial do acessório (conforme consta no datasheet)
  - **quantity**: Quantidade de acessórios que estão presentes em cada solução
> [!NOTE]
> O campo `accessories` é uma lista de acessórios, **mais de um acessório pode ser incluido na mesma solução**.
  
- comments
> [!NOTE]
> O campo `coments` é uma lista de observações importantes para cada solução.
> Ex: limite de potência, compatibilidade entre equipamentos ou qualquer outra informação que julgarmos necessário esclarecer ao cliente .

## Conteúdo dos Arquivos
[`singlePhase_220_HVBat.json`](singlePhaseHVBat.json): Soluções para sistemas **monofásicos 220V**, usando a família **X1-Hybrid-G4** e **Baterias de alta tensão T58**  
[`splitPhase_220V_HVBat.json`](splitPhaseHVBat.json): Soluções para sistemas do tipo **bifásicos 110/220V**, usando a família **X1-SPT** e **Baterias de alta tensão T58**  
[`threePhase_220_HVBat.json`](threePhaseHVBat.json): Soluções para sistemas **trifásicos 220V**, usando a família **X3-Hybrid-G4-LV** e **Baterias de alta tensão T58**  
[`threePhase_380_HVBat.json`](threePhaseHVBat.json): Soluções para sistemas **trifásicos 380V**, usando a família **X3-Hybrid-G4** e **Baterias de alta tensão T58** 

 



import requests
from test_common import *


api_ep_get = 'https://x8ki-letl-twmt.n7.xano.io/api:kOuxY7rb/getSugestao'
header= { 'Content-Type': 'application/json' }
request_payload= { 
    "potencia_nominal":200,
    "potencia_pico":500,
    "consumo_total":3000,
    "matebox":0,
    "tipo":"singlePhase220V",
    "user_id":0
}

if __name__ == "__main__":
    response = requests.post(url=api_ep_get, json=request_payload, headers=header)
    print(response.text)
 

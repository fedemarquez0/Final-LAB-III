import requests

def get_dolar():
    url = "https://free.currconv.com/api/v7/convert?q=USD_ARS&compact=ultra&apiKey=289c397e3d4af2243267"
    respuesta = requests.get(url)
    my_data = respuesta.json()
    valor =  float(my_data['USD_ARS'])
    return valor

def get_valor():
    return 101.8999
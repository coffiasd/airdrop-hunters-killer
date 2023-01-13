import requests


def blockInfo(blocks):
    r = requests.get('http://localhost:8080/blocks?blocks='+blocks)
    return r.json()

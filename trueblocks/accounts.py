import requests

# list transaction index.


def accountList(addrs):
    r = requests.get('http://localhost:8080/list?addrs='+addrs)
    return r.json()

# export detail informations


def accountTransactionsDetail(addrs):
    r = requests.get("")

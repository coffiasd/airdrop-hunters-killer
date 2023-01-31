import requests

# list transaction index.


def accountList(addrs):
    r = requests.get('http://localhost:8080/list?addrs='+addrs+'&cache=true')
    return r.json()

# export detail informations


def accountTransactionsDetail(addrs):
    r = requests.get('http://localhost:8080/export?addrs='+addrs+'&cache=true')
    # print(r.status_code, r.content)
    if r.content == b'':
        return ""
    return r.json()

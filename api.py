from flask import Flask, request, jsonify
from trueblocks import blocks, accounts
from web3 import Web3
from analyze import addrs

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Airdrop-hunter-killer</p>"


@app.route("/analyze", methods=['GET'])
def analyze_address():
    args = request.args
    if "address" not in args:
        data = {'code': 1, 'data': '', 'error': 'Invalid args'}
        return jsonify(data), 400

    address = args["address"]

    if Web3.isAddress(address) == False:
        data = {'code': 1, 'data': '', 'error': 'Invalid args'}
        return jsonify(data), 400

    # get data from trueblock http api.
    x, y, z = addrs.analyzeAddrsScore(address)
    # x<1 y<1 z<0.2
    if x > 1 or y > 1 or z > 0.2:
        data = {'code': 0, 'data': False, 'error': ''}
        return jsonify(data)

    data = {'code': 0, 'data': True, 'error': ''}
    return jsonify(data)

import pandas as pd
from trueblocks import blocks, accounts
from utils import util
from analyze import addrs
import csv
import sys

# Gr15 = pd.read_csv("data/Gr15/GR15_contributions.csv")
# Unicef = pd.read_csv("data/unicef_fantom_grant_rounds/GR15_contributions.csv")
# print(Gr15.info())


def loadGR15Data():
    return pd.read_csv("data/Gr15/GR15_contributions.csv")


def loadFantomData():
    return pd.read_csv("data/Fantom/fantom_grant_votes.csv")


def loadUnicefData():
    return pd.read_csv("data/Unicef/unicef_grant_votes.csv")


def loadResult():
    return pd.read_csv("output/result.csv")


if __name__ == "__main__":
    result = loadResult()
    resultAddrs = result['address'].tolist()

    # fields = ['address', 'activityDegree', 'interactionDiversity', 'interactionDensity']
    filename = "output/result.csv"
    s = 0
    with open(filename, 'a+', newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.writer(csvfile)

        gr15 = loadGR15Data()
        addressArray = gr15["address"].unique()
        for item in addressArray:
            if item in resultAddrs:
                s = s+1
                continue
            x, y, z = addrs.analyzeAddrsScore(item)
            writer.writerow([item, x, y, z])
            s = s+1

    # gr15 = loadGR15Data()
    # addressArray = gr15["address"].unique()
    # for item in addressArray:
    #     if s < 100:
    #         activityDegree = addrs.analyzeAddrsScore(item)
    #     s = s+1
        # activityDegree = addrs.analyzeAddrsActivity(
        #     "0xB315fBA4A6514100BdceA5C438E89dd9dd9F216F")
        # print(activityDegree)

        # for addrs in addressArray:
        # print(gr15.info())
        # count checkout_type
        # count_checkout_type = dict(gr15['checkout_type'].value_counts())
        # {'eth_zksync': 300461, 'eth_std': 107965, 'eth_polygon': 45435, 'celo_std': 2}

        # fantom = loadFantomData()
        # print(fantom.info())
        # count_token = dict(fantom['destination_wallet'].value_counts())
        # print(count_token)
        # {'FTM': 129275, 'WFTM': 6083, 'DAI': 3943, 'BUSD': 36}

        #unicef = loadUnicefData()
        # print(unicef.info())
        #count_token = dict(unicef['token'].value_counts())
        # print(count_token)
        # {'ETH': 58698, 'DAI': 5482}
        # ret = blocks.blockInfo("100")
        # print(ret)
        # accountListJson = accounts.accountList(
        #     "0xB315fBA4A6514100BdceA5C438E89dd9dd9F216F")

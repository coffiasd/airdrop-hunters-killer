import pandas as pd
from trueblocks import blocks, accounts
# Gr15 = pd.read_csv("data/Gr15/GR15_contributions.csv")
# Unicef = pd.read_csv("data/unicef_fantom_grant_rounds/GR15_contributions.csv")
# print(Gr15.info())


def loadGR15Data():
    return pd.read_csv("data/Gr15/GR15_contributions.csv")


def loadFantomData():
    return pd.read_csv("data/Fantom/fantom_grant_votes.csv")


def loadUnicefData():
    return pd.read_csv("data/Unicef/unicef_grant_votes.csv")


if __name__ == "__main__":
    # gr15 = loadGR15Data()
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

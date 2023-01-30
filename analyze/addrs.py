from trueblocks import blocks, accounts
import pandas as pd
import numpy as np
from utils import util
import time


def analyzeAddrsScore(addrs):
    detailJson = accounts.accountTransactionsDetail(addrs)
    if detailJson == "":
        return 0, 0, 0

    data = cleanData(detailJson)

    listDf = pd.DataFrame.from_dict(data)
    firstDate = listDf['timestamp'].min()
    count = listDf['hash'].count()
    # calculate address's lifetime.
    daysCount = util.calculateLifeTime(firstDate)

    # calculate address's activity degree.
    activityDegree = round(count/daysCount, 4)

    # calculate address's Interaction Diversity
    # 去重复统计次数
    methodCount = listDf['method'].unique().size
    interactionDiversity = round(methodCount/daysCount, 4)

    # calculate address's Interaction Density
    # 计算时间间隔，获得最大间隔
    transactionDateCount = listDf['date'].unique().size
    interactionDensity = round(transactionDateCount/daysCount, 4)

    return activityDegree, interactionDiversity, interactionDensity


def cleanData(detailJson):
    data = []
    # print(type(detailJson), detailJson)
    for item in detailJson['data']:
        data.append({
            "method": item['compressedTx'][:10],
            "hash": item['hash'],
            "timestamp": item['timestamp'],
            "date": time.strftime("%Y-%m-%d", time.localtime(item['timestamp']))
        })
    return data

print("Loading datasets... It may take a while.")
from sentiment import sentiment
import pickle
import pandas as pd
import numpy as np
from multiprocessing import cpu_count, Pool


print("The following result should be neg and 1.0")
print(sentiment("He is an incapable person. His projects are totally senseless."))

cores = cpu_count()  # Number of CPU cores on your system
partitions = cores // 2   # Define as many partitions as you want


def parallelize(data, func):
    data_split = np.array_split(data, partitions)
    pool = Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data


def par_func(cs):
    print("Processing batch of", len(cs.index))
    cs["sentiment"] = cs["text"].apply(sentiment)
    return cs


def calculateSentiments():
    print("Reading tweet file")
    with open('./data/Tweets/tweetsblanklines.txt') as IN, open('./data/Tweets/tweets.txt', 'w') as OUT:
        for line in IN:
            if not line.strip(): continue  # skip the empty line
            OUT.write(line)  
    from pathlib import Path
    p = Path('./data/Tweets/tweets.txt')
    p.rename(p.with_suffix('.csv'))
    cs = pd.read_csv("./data/Tweets/tweets.csv")
    print("Total tweets", len(cs.index))
    print("Detecting sentiment in parallel...")
    cs = parallelize(cs, par_func)
    cs.to_csv("./data/Tweets/tweets.csv", index=False)
    print("---------")


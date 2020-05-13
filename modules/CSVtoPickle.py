# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from tqdm import tqdm, tqdm_notebook
tqdm.pandas(tqdm_notebook)

def pickleTweets():
    df = pd.DataFrame()
    d = pd.read_csv(open("./data/Tweets/tweets.csv", 'r'), encoding='utf-8',
                    engine='c', low_memory=False)
    df = pd.concat([d, df])
    print("File rows", len(d.index), "Total rows", len(df.index))


    df.to_pickle('./data/Tweets/all.pickle')  # Save the optimized object

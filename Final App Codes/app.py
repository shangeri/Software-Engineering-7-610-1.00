#The DataFrame plotting methods return a matplotlib AxesSubplot or list of AxesSubplots. (See the docs for plot, or boxplot, for instance.)

#You can then pass that same Axes to the next plotting method (using ax=ax) to draw on the same axes:

import pandas as pd
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
import numpy as np

with open('apple dec sample set.csv', 'r') as f:
    data = list(reader(f))

month = [i[0] for i in data[0::]]

tweets = np.array([i[1] for i in data[0::]])
tweets = tweets.astype(np.float)

volume = np.array([i[2] for i in data[0::]])
volume = volume.astype(np.float)

Apple_Stocks = pd.DataFrame(
    {'month': month,
     'Apple Tweets': tweets})

#right_2014 = pd.DataFrame({'month': ['jan', 'feb'], '2014_val': [4, 5]})

Apple_Volume = pd.DataFrame(
    {'month': month,
     'Apple Volume': volume})

#df_13_14 = pd.merge(left_2013, right_2014, how='outer')
df_merge = pd.merge(Apple_Stocks, Apple_Volume, how='outer')

ax = df_merge[['month', 'Apple Volume']].plot(
    x='month', linestyle='-', marker='o')
df_merge[['month', 'Apple Tweets']].plot(x='month', kind='bar',
                                                        ax=ax)

plt.show()
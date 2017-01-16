#The DataFrame plotting methods return a matplotlib AxesSubplot or list of AxesSubplots. (See the docs for plot, or boxplot, for instance.)

#You can then pass that same Axes to the next plotting method (using ax=ax) to draw on the same axes:

import pandas as pd
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
import numpy as np

from io import StringIO

s = StringIO("""     amount     price
A     40929   4066443
B     93904   9611272
C    188349  19360005
D    248438  24335536
E    205622  18888604
F    140173  12580900
G     76243   6751731
H     36859   3418329
I     29304   2758928
J     39768   3201269
K     30350   2867059""")

df = pd.read_csv(open('apple dec sample set.csv', 'r'), index_col=0, delimiter=',', skipinitialspace=True)

#with open('apple dec sample set.csv', 'r') as f:
#    data = list(reader(f))

#month = [i[0] for i in data[1::]]

#tweets = np.array([i[1] for i in data[1::]])
#tweets = tweets.astype(np.float)

#volume = np.array([i[2] for i in data[1::]])
#volume = volume.astype(np.float)

fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4

df.Tweets.plot(kind='bar', color='red', ax=ax, width=width, position=1)
#df.price.plot(linestyle='-', marker='o', color='blue', ax=ax2, width=width, position=0)
ax2.plot(ax.get_xticks(),df[['Volume']].values, linestyle='-', marker='o', linewidth=2.0)
ax.set_ylabel('Tweets (red)')
ax2.set_ylabel('Volume (blue)')

plt.show()
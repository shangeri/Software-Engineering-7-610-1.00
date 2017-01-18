#The DataFrame plotting methods return a matplotlib AxesSubplot or list of AxesSubplots. (See the docs for plot, or boxplot, for instance.)

#You can then pass that same Axes to the next plotting method (using ax=ax) to draw on the same axes:

import pandas as pd
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
import numpy as np


df = pd.read_csv(open('final tweets data.csv', 'r'), index_col=0, delimiter=',', skipinitialspace=True)
df2 = pd.read_csv(open('final volume data.csv', 'r'), index_col=0, delimiter=',', skipinitialspace=True)


fig = plt.figure() # Create matplotlib figure

ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width = 0.4

df.tweets.plot(kind='bar', color='red', ax=ax, width=width, position=1)
ax2.plot(ax.get_xticks(), df2[['Tesla Trading Volume']].values, linestyle='-', marker='o', linewidth=2.0)
ax.set_ylabel('Number of Tweets (red)')
ax2.set_ylabel('Volume (blue)')

wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()
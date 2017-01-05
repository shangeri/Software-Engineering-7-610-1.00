import pandas as pd
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
from csv import reader
from dateutil import parser

with open('apple dec sample set.csv', 'r') as f:
    data = list(reader(f))

month = [i[0] for i in data[0::]]
stocks = [i[1] for i in data[0::]]

print (month)
print (stocks)
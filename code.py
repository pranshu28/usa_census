import numpy as np
import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv("census_income_learn.csv", header=None)


def headers(file):
    with open(file, 'r') as f:
        h = []
        lines = f.readlines()
        for i in range(142,184):
            temp = lines[i].partition(':')[0]
            if temp[0]=='|':
                i=i-1
                continue
            h.append(temp)
        h.append('Class')
    return h


header = headers("census_income_metadata.txt")
for i in range(df.shape[1]):
    print(df[i].dtype)
    if df[i].dtype == 'int64' or df[i].dtype == 'float64':
        print(plt.hist(df[i]))
    else:
        print()
    df = df.rename(columns={i: header[i]})
# plt.hist(df[0])
# plt.boxplot(df[0])
plt.show()

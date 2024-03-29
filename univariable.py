import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv("/home/pranshu/Documents/Projects/census_income_learn.csv", header=None)


def headers(file):
    with open(file, 'r') as f:
        h = []
        lines = f.readlines()
        for i in range(142, 184):
            temp = lines[i].partition(':')[0]
            if temp[0] == '|':
                i = i - 1
                continue
            h.append(temp)
        h.append('Class')
    return h


header = headers("census_income_metadata.txt")
continuous = ['age', 'wage per hour', 'capital gains', 'capital losses', 'dividends from stocks', 'instance weight',
              'num persons worked for employer', 'weeks worked in year']


def plot_(fig, l1, l2, t):
    plt.figure(fig)
    plt.xlabel(l1)
    plt.ylabel(l2)
    plt.title(t)


j = 0

for i in range(df.shape[1]):
    df = df.rename(columns={i: header[i]})
    if header[i] in continuous:
        dist = df[header[i]].sort_values()
        plot_(j, 'values', header[i], header[i])
        dist.plot.hist(bins=20)
        plt.figtext(1, 0.4, df[header[i]].describe())
    else:
        dist = df[header[i]].value_counts(sort=False)
        miss = [' Not in universe', ' ?', ' Not in universe or children', ' Not in universe under 1 year old']
        m = 0
        for k in miss:
            if k in dist.index.tolist():
                m = +dist[k]
                dist = dist.drop(k)
        dist = dist * 100. / df.shape[0]
        if df[header[i]].dtype == 'int64':
            plot_(j, 'categories', 'Frequency', header[i])
            df[header[i]].hist(bins=50)
        else:
            plot_(j, 'categories', 'Percentage', header[i])
            dist.plot.bar()
        plt.figtext(0.3, 1, 'Missing values: ' + str(m) + ' (' + str(m * 100. / df.shape[0]) + ' % )')
    plt.savefig('pics/' + header[i] + '.png', bbox_inches='tight')
    j += 1
# plt.show()

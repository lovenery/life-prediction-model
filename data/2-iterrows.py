# https://pandas.pydata.org/pandas-docs/stable/merging.html

# Read CSV
import pandas as pd
import os.path as path
df = pd.read_csv(path.join(path.dirname(__file__), './merged.csv'))


# Clock
from datetime import datetime
t0 = datetime.now()


# iterrows
XX = pd.DataFrame()
for index, row in df.iterrows():
    # s = {
    #     'county': row['county'],
    #     'sex': row['sex'],
    #     'cause': row['cause'],
    #     'age': row['age_code']
    # }
    # for i in range(getattr(row, 'N')):
    #     XX = XX.append(s, ignore_index=True)
    XX = XX.append([row] * getattr(row, 'N'), ignore_index=True)
    if index == 1000:
        break
    # if index % 10000 == 0:
    #     print "10000 iter passed"
    #     print "remain %d times" % (310430 - index)
    #     print "Already run %0.1f seconds" % (datetime.now() - t0).total_seconds()


# print(df[ df['age_code'] == 99 ])
print(XX)
print "Finish...already run %0.2f seconds" % (datetime.now() - t0).total_seconds()
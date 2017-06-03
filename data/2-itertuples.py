# https://pandas.pydata.org/pandas-docs/stable/merging.html

# import merge
# merge.start()

# Read CSV
import pandas as pd
import os.path as path
df = pd.read_csv(path.join(path.dirname(__file__), './merged.csv'))


# Clock
from datetime import datetime
t0 = datetime.now()


# itertuples
XX = pd.DataFrame()
index = 0
for row in df.itertuples():
    index += 1
    # s = pd.Series({
    #     'county': getattr(row, 'county'),
    #     'sex': getattr(row, 'sex'),
    #     'cause': getattr(row, 'cause'),
    #     'age_code': getattr(row, 'age_code')
    # })
    # for i in range(getattr(row, 'N')):
    #     XX = XX.append(s, ignore_index=True)

    XX = XX.append([row] * getattr(row, 'N'), ignore_index=True)

    if index == 1000:
        break
    # if index % 10000 == 0:
    #     print "10000 iter passed"
    #     print "remain %d times" % (310430 - index)
    #     print "Already run %0.1f seconds" % (datetime.now() - t0).total_seconds()


# Cut
Z = pd.DataFrame()
Z['county'] = XX['county']
Z['sex'] = XX['sex']
Z['cause'] = XX['cause']
Z['age'] = XX['age_code']
# Z.to_csv(path.join(path.dirname(__file__), './data.csv'), index=False)


# Result
print(Z)
print "Finish...already run %0.2f seconds" % (datetime.now() - t0).total_seconds()
